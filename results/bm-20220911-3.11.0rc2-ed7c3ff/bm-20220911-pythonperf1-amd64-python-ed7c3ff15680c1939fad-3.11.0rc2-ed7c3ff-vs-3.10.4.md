
# Results vs. 3.10.4

- fork: python
- ref: ed7c3ff15680c1939fad
- machine: windows-amd64
- commit hash: ed7c3ff
- commit date: 2022-09-11
- overall geometric mean: 1.12x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 202 ms: 1.17x faster                                                        |
| chameleon      | 5.92 ms                                                     | 5.09 ms: 1.16x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.57 sec: 1.20x faster                                                      |
| html5lib       | 46.5 ms                                                     | 37.2 ms: 1.25x faster                                                       |
| tornado_http   | 109 ms                                                      | 92.1 ms: 1.19x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.9 ms: 1.12x faster                                                       |
| nbody          | 69.3 ms                                                     | 68.6 ms: 1.01x faster                                                       |
| pidigits       | 145 ms                                                      | 147 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 89.5 ms: 1.16x faster                                                       |
| regex_dna      | 132 ms                                                      | 115 ms: 1.15x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 13.4 ms: 1.12x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 257 us                                                      | 197 us: 1.30x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.9 ms: 1.21x faster                                                       |
| unpickle             | 9.17 us                                                     | 7.70 us: 1.19x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 149 us: 1.15x faster                                                        |
| xml_etree_parse      | 102 ms                                                      | 91.6 ms: 1.11x faster                                                       |
| json_dumps           | 8.50 ms                                                     | 7.66 ms: 1.11x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.55 us: 1.10x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 51.2 ms: 1.07x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.04x faster                                                       |
| pickle               | 6.80 us                                                     | 6.60 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 61.9 ms: 1.03x faster                                                       |
| pickle_list          | 2.59 us                                                     | 2.65 us: 1.02x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.2 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.5 ms: 1.08x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 7.22 ms: 1.22x faster                                                       |
| django_template | 28.2 ms                                                     | 23.8 ms: 1.18x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 16.7 ms: 1.14x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 38.3 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.61 ms: 1.60x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 740 ms: 1.44x faster                                                        |
| go                      | 136 ms                                                      | 97.5 ms: 1.40x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 70.9 ns: 1.36x faster                                                       |
| scimark_sor             | 105 ms                                                      | 77.3 ms: 1.36x faster                                                       |
| async_tree_none         | 420 ms                                                      | 310 ms: 1.35x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 368 ms: 1.35x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 63.4 ms: 1.35x faster                                                       |
| richards                | 41.2 ms                                                     | 30.6 ms: 1.35x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 920 us: 1.33x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.12 ms: 1.31x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 197 us: 1.30x faster                                                        |
| raytrace                | 271 ms                                                      | 211 ms: 1.29x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 48.5 ms: 1.29x faster                                                       |
| pyflate                 | 387 ms                                                      | 303 ms: 1.28x faster                                                        |
| async_generators        | 224 ms                                                      | 176 ms: 1.27x faster                                                        |
| mypy2                   | 352 ms                                                      | 276 ms: 1.27x faster                                                        |
| pycparser               | 868 ms                                                      | 683 ms: 1.27x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 44.6 ms: 1.25x faster                                                       |
| thrift                  | 615 us                                                      | 491 us: 1.25x faster                                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 488 ms: 1.25x faster                                                        |
| html5lib                | 46.5 ms                                                     | 37.2 ms: 1.25x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 4.48 ms: 1.23x faster                                                       |
| chaos                   | 58.9 ms                                                     | 48.0 ms: 1.23x faster                                                       |
| mako                    | 8.80 ms                                                     | 7.22 ms: 1.22x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 35.9 ms: 1.21x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.57 sec: 1.20x faster                                                      |
| unpickle                | 9.17 us                                                     | 7.70 us: 1.19x faster                                                       |
| tornado_http            | 109 ms                                                      | 92.1 ms: 1.19x faster                                                       |
| django_template         | 28.2 ms                                                     | 23.8 ms: 1.18x faster                                                       |
| aiohttp                 | 1.01 ms                                                     | 857 us: 1.18x faster                                                        |
| 2to3                    | 237 ms                                                      | 202 ms: 1.17x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 667 us: 1.17x faster                                                        |
| sqlalchemy_declarative  | 95.4 ms                                                     | 81.7 ms: 1.17x faster                                                       |
| chameleon               | 5.92 ms                                                     | 5.09 ms: 1.16x faster                                                       |
| regex_compile           | 103 ms                                                      | 89.5 ms: 1.16x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 512 ms: 1.15x faster                                                        |
| regex_dna               | 132 ms                                                      | 115 ms: 1.15x faster                                                        |
| pprint_pformat          | 1.21 sec                                                    | 1.05 sec: 1.15x faster                                                      |
| unpickle_pure_python    | 171 us                                                      | 149 us: 1.15x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 34.0 ms: 1.14x faster                                                       |
| dask                    | 305 ms                                                      | 267 ms: 1.14x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 16.7 ms: 1.14x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 13.4 ms: 1.12x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 25.4 us: 1.12x faster                                                       |
| float                   | 60.2 ms                                                     | 53.9 ms: 1.12x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 849 us: 1.11x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 91.6 ms: 1.11x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 7.66 ms: 1.11x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.55 us: 1.10x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.67 us: 1.10x faster                                                       |
| pylint                  | 347 ms                                                      | 316 ms: 1.10x faster                                                        |
| sympy_integrate         | 14.8 ms                                                     | 13.5 ms: 1.09x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 43.6 ms: 1.09x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 186 ms: 1.09x faster                                                        |
| python_startup          | 20.0 ms                                                     | 18.5 ms: 1.08x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.59 sec: 1.08x faster                                                      |
| deepcopy_reduce         | 2.16 us                                                     | 2.00 us: 1.08x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 72.1 ms: 1.07x faster                                                       |
| sympy_expand            | 315 ms                                                      | 294 ms: 1.07x faster                                                        |
| coroutines              | 15.9 ms                                                     | 14.9 ms: 1.07x faster                                                       |
| deepcopy                | 255 us                                                      | 239 us: 1.07x faster                                                        |
| sqlalchemy_imperative   | 11.0 ms                                                     | 10.3 ms: 1.07x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 73.2 ms: 1.07x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 51.2 ms: 1.07x faster                                                       |
| sympy_sum               | 104 ms                                                      | 98.2 ms: 1.06x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 38.3 ms: 1.06x faster                                                       |
| comprehensions          | 16.0 us                                                     | 15.2 us: 1.05x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 64.6 ms: 1.04x faster                                                       |
| json_loads              | 14.2 us                                                     | 13.7 us: 1.04x faster                                                       |
| sympy_str               | 188 ms                                                      | 182 ms: 1.03x faster                                                        |
| pickle                  | 6.80 us                                                     | 6.60 us: 1.03x faster                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 61.9 ms: 1.03x faster                                                       |
| scimark_fft             | 193 ms                                                      | 189 ms: 1.02x faster                                                        |
| python_startup_no_site  | 15.5 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| nbody                   | 69.3 ms                                                     | 68.6 ms: 1.01x faster                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 61.2 ms: 1.01x slower                                                       |
| pidigits                | 145 ms                                                      | 147 ms: 1.01x slower                                                        |
| pickle_list             | 2.59 us                                                     | 2.65 us: 1.02x slower                                                       |
| meteor_contest          | 72.5 ms                                                     | 74.3 ms: 1.02x slower                                                       |
| telco                   | 3.78 ms                                                     | 3.91 ms: 1.03x slower                                                       |
| logging_format          | 6.66 us                                                     | 6.97 us: 1.05x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.41 ms: 1.05x slower                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.81 ms: 1.06x slower                                                       |
| logging_simple          | 6.20 us                                                     | 6.57 us: 1.06x slower                                                       |
| generators              | 31.6 ms                                                     | 33.5 ms: 1.06x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.2 us: 1.07x slower                                                       |
| unpack_sequence         | 37.8 ns                                                     | 42.7 ns: 1.13x slower                                                       |
| coverage                | 40.0 ms                                                     | 53.2 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (4): asyncio_tcp, fannkuch, flaskblogging, json
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

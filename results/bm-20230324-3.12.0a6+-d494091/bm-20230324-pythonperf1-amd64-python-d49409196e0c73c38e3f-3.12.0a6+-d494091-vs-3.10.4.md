
# Results vs. 3.10.4

- fork: python
- ref: d49409196e0c73c38e3f
- machine: windows-amd64
- commit hash: d494091
- commit date: 2023-03-24
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 194 ms: 1.22x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.30 ms: 1.38x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.51 sec: 1.25x faster                                                      |
| html5lib       | 46.5 ms                                                     | 35.5 ms: 1.31x faster                                                       |
| tornado_http   | 109 ms                                                      | 86.7 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 46.0 ms: 1.31x faster                                                       |
| nbody          | 69.3 ms                                                     | 55.6 ms: 1.25x faster                                                       |
| pidigits       | 145 ms                                                      | 146 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 79.6 ms: 1.30x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| regex_dna      | 132 ms                                                      | 122 ms: 1.08x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.83 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.44 ms: 1.56x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 168 us: 1.52x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 117 us: 1.46x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 33.9 ms: 1.28x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 87.3 ms: 1.17x faster                                                       |
| unpickle             | 9.17 us                                                     | 7.96 us: 1.15x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 50.0 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 59.2 ms: 1.07x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.4 us: 1.06x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.70 us: 1.04x faster                                                       |
| pickle               | 6.80 us                                                     | 6.65 us: 1.02x faster                                                       |
| pickle_list          | 2.59 us                                                     | 2.78 us: 1.07x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.6 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.10 ms: 1.44x faster                                                       |
| django_template | 28.2 ms                                                     | 19.9 ms: 1.42x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 13.8 ms: 1.38x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 30.5 ms: 1.33x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.39x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.91 ms: 2.18x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 54.5 ns: 1.77x faster                                                       |
| richards                | 41.2 ms                                                     | 24.3 ms: 1.69x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 50.5 ms: 1.69x faster                                                       |
| go                      | 136 ms                                                      | 80.6 ms: 1.69x faster                                                       |
| mypy2                   | 352 ms                                                      | 209 ms: 1.68x faster                                                        |
| raytrace                | 271 ms                                                      | 164 ms: 1.65x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.44 ms: 1.56x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 168 us: 1.52x faster                                                        |
| asyncio_tcp             | 712 ms                                                      | 469 ms: 1.52x faster                                                        |
| generators              | 31.6 ms                                                     | 20.9 ms: 1.51x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.66 ms: 1.51x faster                                                       |
| chaos                   | 58.9 ms                                                     | 39.6 ms: 1.49x faster                                                       |
| scimark_sor             | 105 ms                                                      | 70.6 ms: 1.49x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 723 ms: 1.47x faster                                                        |
| unpickle_pure_python    | 171 us                                                      | 117 us: 1.46x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 19.6 us: 1.45x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 843 us: 1.45x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.10 ms: 1.44x faster                                                       |
| pyflate                 | 387 ms                                                      | 271 ms: 1.43x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 349 ms: 1.42x faster                                                        |
| async_tree_none         | 420 ms                                                      | 295 ms: 1.42x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 39.3 ms: 1.42x faster                                                       |
| django_template         | 28.2 ms                                                     | 19.9 ms: 1.42x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.03 ms: 1.42x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 44.3 ms: 1.41x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 27.4 ns: 1.38x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.30 ms: 1.38x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 13.8 ms: 1.38x faster                                                       |
| pycparser               | 868 ms                                                      | 640 ms: 1.36x faster                                                        |
| thrift                  | 615 us                                                      | 459 us: 1.34x faster                                                        |
| pprint_pformat          | 1.21 sec                                                    | 902 ms: 1.34x faster                                                        |
| pprint_safe_repr        | 589 ms                                                      | 443 ms: 1.33x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 30.5 ms: 1.33x faster                                                       |
| float                   | 60.2 ms                                                     | 46.0 ms: 1.31x faster                                                       |
| html5lib                | 46.5 ms                                                     | 35.5 ms: 1.31x faster                                                       |
| regex_compile           | 103 ms                                                      | 79.6 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 473 ms: 1.29x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 33.9 ms: 1.28x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 61.1 ms: 1.28x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 30.8 ms: 1.27x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.36 sec: 1.26x faster                                                      |
| tornado_http            | 109 ms                                                      | 86.7 ms: 1.26x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.51 sec: 1.25x faster                                                      |
| deepcopy                | 255 us                                                      | 204 us: 1.25x faster                                                        |
| nbody                   | 69.3 ms                                                     | 55.6 ms: 1.25x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 54.1 ms: 1.24x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 166 ms: 1.22x faster                                                        |
| 2to3                    | 237 ms                                                      | 194 ms: 1.22x faster                                                        |
| scimark_fft             | 193 ms                                                      | 159 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.20 ms: 1.21x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.82 us: 1.19x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 87.3 ms: 1.17x faster                                                       |
| sympy_expand            | 315 ms                                                      | 271 ms: 1.16x faster                                                        |
| fannkuch                | 258 ms                                                      | 222 ms: 1.16x faster                                                        |
| sympy_integrate         | 14.8 ms                                                     | 12.8 ms: 1.16x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 818 us: 1.16x faster                                                        |
| unpickle                | 9.17 us                                                     | 7.96 us: 1.15x faster                                                       |
| coroutines              | 15.9 ms                                                     | 13.9 ms: 1.14x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 42.1 ms: 1.13x faster                                                       |
| json                    | 3.05 ms                                                     | 2.71 ms: 1.13x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 698 us: 1.12x faster                                                        |
| sympy_str               | 188 ms                                                      | 169 ms: 1.11x faster                                                        |
| async_generators        | 224 ms                                                      | 202 ms: 1.11x faster                                                        |
| python_startup          | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 50.0 ms: 1.09x faster                                                       |
| sympy_sum               | 104 ms                                                      | 95.6 ms: 1.09x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| regex_dna               | 132 ms                                                      | 122 ms: 1.08x faster                                                        |
| comprehensions          | 16.0 us                                                     | 14.8 us: 1.08x faster                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 59.2 ms: 1.07x faster                                                       |
| json_loads              | 14.2 us                                                     | 13.4 us: 1.06x faster                                                       |
| logging_simple          | 6.20 us                                                     | 5.91 us: 1.05x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.76 us: 1.04x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.70 us: 1.04x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.41 us: 1.04x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 70.4 ms: 1.03x faster                                                       |
| pickle                  | 6.80 us                                                     | 6.65 us: 1.02x faster                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| pidigits                | 145 ms                                                      | 146 ms: 1.00x slower                                                        |
| telco                   | 3.78 ms                                                     | 3.85 ms: 1.02x slower                                                       |
| pathlib                 | 77.4 ms                                                     | 82.2 ms: 1.06x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 64.8 ms: 1.07x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.78 us: 1.07x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.47 ms: 1.09x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.6 us: 1.10x slower                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.83 ms: 1.10x slower                                                       |
| dask                    | 305 ms                                                      | 353 ms: 1.16x slower                                                        |
| coverage                | 40.0 ms                                                     | 50.1 ms: 1.25x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.24x faster                                                                |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

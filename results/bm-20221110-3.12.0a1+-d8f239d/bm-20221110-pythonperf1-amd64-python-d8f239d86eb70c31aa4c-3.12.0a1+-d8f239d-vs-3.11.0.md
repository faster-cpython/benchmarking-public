
# Results vs. 3.11.0

- fork: python
- ref: d8f239d86eb70c31aa4c
- machine: windows-amd64
- commit hash: d8f239d
- commit date: 2022-11-10
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 203 ms: 1.03x faster                                                        |
| chameleon      | 5.11 ms                                                     | 5.01 ms: 1.02x faster                                                       |
| html5lib       | 37.5 ms                                                     | 34.8 ms: 1.08x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 93.3 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 63.5 ms: 1.10x faster                                                       |
| float          | 54.6 ms                                                     | 53.0 ms: 1.03x faster                                                       |
| pidigits       | 148 ms                                                      | 153 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 85.4 ms: 1.06x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.6 ms: 1.01x faster                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.52 ms: 1.37x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 138 us: 1.10x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 91.7 ms: 1.05x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 36.6 ms: 1.01x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.6 ms: 1.01x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 198 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.9 ms: 1.02x slower                                                       |
| json_loads           | 12.9 us                                                     | 13.2 us: 1.02x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.2 us: 1.04x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.88 us: 1.07x slower                                                       |
| pickle               | 6.61 us                                                     | 7.20 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.26 ms                                                     | 6.42 ms: 1.13x faster                                                       |
| django_template | 24.1 ms                                                     | 22.0 ms: 1.09x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 35.5 ms: 1.05x faster                                                       |
| genshi_text     | 17.0 ms                                                     | 16.1 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 7.56 ms                                                     | 5.52 ms: 1.37x faster                                                       |
| unpack_sequence         | 46.1 ns                                                     | 35.5 ns: 1.30x faster                                                       |
| json                    | 3.25 ms                                                     | 2.75 ms: 1.18x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.42 ms: 1.13x faster                                                       |
| richards                | 30.6 ms                                                     | 27.6 ms: 1.11x faster                                                       |
| raytrace                | 211 ms                                                      | 191 ms: 1.10x faster                                                        |
| nbody                   | 70.0 ms                                                     | 63.5 ms: 1.10x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 138 us: 1.10x faster                                                        |
| django_template         | 24.1 ms                                                     | 22.0 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.35 ms: 1.09x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 32.2 ms: 1.08x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.42 ms: 1.08x faster                                                       |
| html5lib                | 37.5 ms                                                     | 34.8 ms: 1.08x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 23.4 us: 1.08x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 60.4 ms: 1.07x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.09 ms: 1.07x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 65.3 ns: 1.07x faster                                                       |
| fannkuch                | 252 ms                                                      | 236 ms: 1.07x faster                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.95 us: 1.07x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 85.4 ms: 1.06x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 4.30 ms: 1.06x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 70.7 ms: 1.06x faster                                                       |
| deepcopy                | 246 us                                                      | 232 us: 1.06x faster                                                        |
| go                      | 97.3 ms                                                     | 92.1 ms: 1.06x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 485 ms: 1.05x faster                                                        |
| pyflate                 | 304 ms                                                      | 289 ms: 1.05x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 35.5 ms: 1.05x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 16.1 ms: 1.05x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 42.5 ms: 1.05x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 907 us: 1.05x faster                                                        |
| mdp                     | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                      |
| sqlglot_normalize       | 190 ms                                                      | 182 ms: 1.05x faster                                                        |
| xml_etree_parse         | 95.9 ms                                                     | 91.7 ms: 1.05x faster                                                       |
| pycparser               | 691 ms                                                      | 662 ms: 1.04x faster                                                        |
| scimark_fft             | 178 ms                                                      | 171 ms: 1.04x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 45.9 ms: 1.04x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 1.00 sec: 1.03x faster                                                      |
| dulwich_log             | 44.5 ms                                                     | 43.1 ms: 1.03x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 65.8 ms: 1.03x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.4 ms: 1.03x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 61.5 ms: 1.03x faster                                                       |
| 2to3                    | 209 ms                                                      | 203 ms: 1.03x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.79 ms: 1.03x faster                                                       |
| float                   | 54.6 ms                                                     | 53.0 ms: 1.03x faster                                                       |
| chaos                   | 47.1 ms                                                     | 45.9 ms: 1.03x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.85 us: 1.02x faster                                                       |
| chameleon               | 5.11 ms                                                     | 5.01 ms: 1.02x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.49 us: 1.02x faster                                                       |
| sympy_expand            | 295 ms                                                      | 290 ms: 1.02x faster                                                        |
| coverage                | 55.9 ms                                                     | 54.9 ms: 1.02x faster                                                       |
| regex_v8                | 13.8 ms                                                     | 13.6 ms: 1.01x faster                                                       |
| mypy2                   | 229 ms                                                      | 226 ms: 1.01x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 36.6 ms: 1.01x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 51.6 ms: 1.01x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 198 us: 1.01x faster                                                        |
| sympy_str               | 182 ms                                                      | 180 ms: 1.01x faster                                                        |
| coroutines              | 14.6 ms                                                     | 14.5 ms: 1.01x faster                                                       |
| async_generators        | 178 ms                                                      | 176 ms: 1.01x faster                                                        |
| async_tree_io           | 779 ms                                                      | 788 ms: 1.01x slower                                                        |
| tornado_http            | 91.8 ms                                                     | 93.3 ms: 1.02x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 63.5 ms: 1.02x slower                                                       |
| generators              | 33.8 ms                                                     | 34.4 ms: 1.02x slower                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.9 ms: 1.02x slower                                                       |
| json_loads              | 12.9 us                                                     | 13.2 us: 1.02x slower                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                                       |
| thrift                  | 491 us                                                      | 505 us: 1.03x slower                                                        |
| async_tree_none         | 320 ms                                                      | 330 ms: 1.03x slower                                                        |
| pidigits                | 148 ms                                                      | 153 ms: 1.03x slower                                                        |
| pickle_dict             | 18.5 us                                                     | 19.2 us: 1.04x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 74.2 ms: 1.04x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                       |
| regex_dna               | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| async_tree_memoization  | 371 ms                                                      | 394 ms: 1.06x slower                                                        |
| asyncio_tcp             | 699 ms                                                      | 745 ms: 1.07x slower                                                        |
| sqlite_synth            | 1.68 us                                                     | 1.80 us: 1.07x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.88 us: 1.07x slower                                                       |
| pickle                  | 6.61 us                                                     | 7.20 us: 1.09x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (12): dask, docutils, sympy_sum, scimark_sor, comprehensions, create_gc_cycles, python_startup_no_site, unpickle_list, python_startup, bench_thread_pool, async_tree_cpu_io_mixed, unpickle
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

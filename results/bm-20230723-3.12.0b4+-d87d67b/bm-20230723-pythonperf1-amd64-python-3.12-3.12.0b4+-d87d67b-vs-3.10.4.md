
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: d87d67b
- commit date: 2023-07-23
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 209 ms: 1.13x faster                                        |
| docutils       | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                      |
| tornado_http   | 109 ms                                                      | 87.1 ms: 1.25x faster                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 52.1 ms: 1.15x faster                                       |
| nbody          | 69.3 ms                                                     | 66.9 ms: 1.04x faster                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 85.7 ms: 1.21x faster                                       |
| regex_v8       | 15.0 ms                                                     | 14.0 ms: 1.07x faster                                       |
| regex_dna      | 132 ms                                                      | 123 ms: 1.07x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.67 ms: 1.50x faster                                       |
| pickle_pure_python   | 257 us                                                      | 189 us: 1.36x faster                                        |
| unpickle_pure_python | 171 us                                                      | 129 us: 1.33x faster                                        |
| tomli_loads          | 1.62 sec                                                    | 1.34 sec: 1.21x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 37.0 ms: 1.17x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 91.3 ms: 1.11x faster                                       |
| unpickle             | 9.17 us                                                     | 8.34 us: 1.10x faster                                       |
| json_loads           | 14.2 us                                                     | 13.6 us: 1.04x faster                                       |
| pickle               | 6.80 us                                                     | 7.12 us: 1.05x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.6 us: 1.10x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.90 us: 1.12x slower                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                |

Benchmark hidden because not significant (3): unpickle_list, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.6 ms: 1.08x faster                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.77 ms: 1.30x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4+-d87d67b |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 92.0 us: 3.53x faster                                       |
| deltablue                | 4.17 ms                                                     | 2.06 ms: 2.03x faster                                       |
| richards_super           | 51.7 ms                                                     | 29.4 ms: 1.76x faster                                       |
| mypy2                    | 352 ms                                                      | 209 ms: 1.68x faster                                        |
| logging_silent           | 96.4 ns                                                     | 58.1 ns: 1.66x faster                                       |
| go                       | 136 ms                                                      | 85.9 ms: 1.58x faster                                       |
| richards                 | 41.2 ms                                                     | 26.0 ms: 1.58x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 785 us: 1.55x faster                                        |
| async_tree_io            | 1.07 sec                                                    | 697 ms: 1.53x faster                                        |
| asyncio_tcp              | 712 ms                                                      | 470 ms: 1.52x faster                                        |
| scimark_lu               | 85.4 ms                                                     | 56.5 ms: 1.51x faster                                       |
| async_tree_memoization   | 497 ms                                                      | 331 ms: 1.50x faster                                        |
| json_dumps               | 8.50 ms                                                     | 5.67 ms: 1.50x faster                                       |
| raytrace                 | 271 ms                                                      | 182 ms: 1.49x faster                                        |
| generators               | 31.6 ms                                                     | 21.5 ms: 1.47x faster                                       |
| async_tree_none          | 420 ms                                                      | 285 ms: 1.47x faster                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 996 us: 1.47x faster                                        |
| hexiom                   | 5.52 ms                                                     | 3.90 ms: 1.41x faster                                       |
| chaos                    | 58.9 ms                                                     | 42.6 ms: 1.38x faster                                       |
| pickle_pure_python       | 257 us                                                      | 189 us: 1.36x faster                                        |
| crypto_pyaes             | 62.3 ms                                                     | 46.4 ms: 1.34x faster                                       |
| pyflate                  | 387 ms                                                      | 289 ms: 1.34x faster                                        |
| scimark_sor              | 105 ms                                                      | 78.5 ms: 1.34x faster                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 41.8 ms: 1.34x faster                                       |
| unpickle_pure_python     | 171 us                                                      | 129 us: 1.33x faster                                        |
| pycparser                | 868 ms                                                      | 665 ms: 1.30x faster                                        |
| mako                     | 8.80 ms                                                     | 6.77 ms: 1.30x faster                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 469 ms: 1.30x faster                                        |
| mdp                      | 1.71 sec                                                    | 1.34 sec: 1.28x faster                                      |
| spectral_norm            | 78.0 ms                                                     | 61.6 ms: 1.27x faster                                       |
| tornado_http             | 109 ms                                                      | 87.1 ms: 1.25x faster                                       |
| deepcopy_memo            | 28.5 us                                                     | 23.4 us: 1.22x faster                                       |
| tomli_loads              | 1.62 sec                                                    | 1.34 sec: 1.21x faster                                      |
| regex_compile            | 103 ms                                                      | 85.7 ms: 1.21x faster                                       |
| aiohttp                  | 1.01 ms                                                     | 850 us: 1.19x faster                                        |
| docutils                 | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                      |
| sqlglot_optimize         | 39.0 ms                                                     | 33.1 ms: 1.18x faster                                       |
| xml_etree_process        | 43.4 ms                                                     | 37.0 ms: 1.17x faster                                       |
| pprint_pformat           | 1.21 sec                                                    | 1.03 sec: 1.17x faster                                      |
| pprint_safe_repr         | 589 ms                                                      | 508 ms: 1.16x faster                                        |
| comprehensions           | 16.0 us                                                     | 13.8 us: 1.16x faster                                       |
| float                    | 60.2 ms                                                     | 52.1 ms: 1.15x faster                                       |
| bench_thread_pool        | 946 us                                                      | 821 us: 1.15x faster                                        |
| coroutines               | 15.9 ms                                                     | 14.0 ms: 1.14x faster                                       |
| sqlglot_normalize        | 202 ms                                                      | 177 ms: 1.14x faster                                        |
| 2to3                     | 237 ms                                                      | 209 ms: 1.13x faster                                        |
| deepcopy                 | 255 us                                                      | 228 us: 1.12x faster                                        |
| scimark_fft              | 193 ms                                                      | 172 ms: 1.12x faster                                        |
| xml_etree_parse          | 102 ms                                                      | 91.3 ms: 1.11x faster                                       |
| nqueens                  | 67.0 ms                                                     | 60.6 ms: 1.11x faster                                       |
| dulwich_log              | 47.6 ms                                                     | 43.1 ms: 1.11x faster                                       |
| unpickle                 | 9.17 us                                                     | 8.34 us: 1.10x faster                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.45 ms: 1.09x faster                                       |
| create_gc_cycles         | 782 us                                                      | 721 us: 1.08x faster                                        |
| python_startup           | 20.0 ms                                                     | 18.6 ms: 1.08x faster                                       |
| fannkuch                 | 258 ms                                                      | 240 ms: 1.07x faster                                        |
| regex_v8                 | 15.0 ms                                                     | 14.0 ms: 1.07x faster                                       |
| regex_dna                | 132 ms                                                      | 123 ms: 1.07x faster                                        |
| sqlite_synth             | 1.84 us                                                     | 1.74 us: 1.06x faster                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.04 us: 1.06x faster                                       |
| json_loads               | 14.2 us                                                     | 13.6 us: 1.04x faster                                       |
| json                     | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                       |
| nbody                    | 69.3 ms                                                     | 66.9 ms: 1.04x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                       |
| async_generators         | 224 ms                                                      | 225 ms: 1.01x slower                                        |
| meteor_contest           | 72.5 ms                                                     | 73.4 ms: 1.01x slower                                       |
| pathlib                  | 77.4 ms                                                     | 78.9 ms: 1.02x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.35 us: 1.02x slower                                       |
| logging_format           | 6.66 us                                                     | 6.83 us: 1.03x slower                                       |
| pidigits                 | 145 ms                                                      | 151 ms: 1.04x slower                                        |
| pickle                   | 6.80 us                                                     | 7.12 us: 1.05x slower                                       |
| unpack_sequence          | 37.8 ns                                                     | 39.7 ns: 1.05x slower                                       |
| telco                    | 3.78 ms                                                     | 4.05 ms: 1.07x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.47 ms: 1.09x slower                                       |
| pickle_dict              | 16.9 us                                                     | 18.6 us: 1.10x slower                                       |
| bench_mp_pool            | 60.7 ms                                                     | 67.2 ms: 1.11x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.90 us: 1.12x slower                                       |
| dask                     | 305 ms                                                      | 358 ms: 1.17x slower                                        |
| coverage                 | 40.0 ms                                                     | 50.3 ms: 1.26x slower                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                |

Benchmark hidden because not significant (5): asyncio_tcp_ssl, unpickle_list, xml_etree_iterparse, xml_etree_generate, python_startup_no_site
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift

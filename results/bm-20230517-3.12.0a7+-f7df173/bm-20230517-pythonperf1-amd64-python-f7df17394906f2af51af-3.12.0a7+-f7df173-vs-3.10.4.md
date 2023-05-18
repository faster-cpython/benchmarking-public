
# Results vs. 3.10.4

- fork: python
- ref: f7df17394906f2af51af
- machine: windows-amd64
- commit hash: f7df173
- commit date: 2023-05-17
- overall geometric mean: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 211 ms: 1.12x faster                                                        |
| docutils       | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                                      |
| tornado_http   | 109 ms                                                      | 89.5 ms: 1.22x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.3 ms: 1.11x faster                                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 85.5 ms: 1.21x faster                                                       |
| regex_dna      | 132 ms                                                      | 117 ms: 1.13x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 14.3 ms: 1.05x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.51 ms: 1.54x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 191 us: 1.34x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 131 us: 1.30x faster                                                        |
| tomli_loads          | 1.62 sec                                                    | 1.33 sec: 1.22x faster                                                      |
| xml_etree_process    | 43.4 ms                                                     | 38.1 ms: 1.14x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.13 us: 1.13x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 91.5 ms: 1.11x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.3 us: 1.06x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 56.7 ms: 1.04x slower                                                       |
| pickle               | 6.80 us                                                     | 7.12 us: 1.05x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.6 us: 1.10x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.86 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.5 ms: 1.02x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.61 ms: 1.33x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230517-pythonperf1-amd64-python-f7df17394906f2af51af-3.12.0a7+-f7df173 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 99.4 us: 3.27x faster                                                       |
| deltablue                | 4.17 ms                                                     | 2.07 ms: 2.02x faster                                                       |
| richards_super           | 51.7 ms                                                     | 29.4 ms: 1.76x faster                                                       |
| mypy2                    | 352 ms                                                      | 213 ms: 1.65x faster                                                        |
| richards                 | 41.2 ms                                                     | 25.5 ms: 1.62x faster                                                       |
| logging_silent           | 96.4 ns                                                     | 60.7 ns: 1.59x faster                                                       |
| go                       | 136 ms                                                      | 86.8 ms: 1.57x faster                                                       |
| json_dumps               | 8.50 ms                                                     | 5.51 ms: 1.54x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 794 us: 1.54x faster                                                        |
| scimark_lu               | 85.4 ms                                                     | 56.3 ms: 1.52x faster                                                       |
| asyncio_tcp              | 712 ms                                                      | 470 ms: 1.52x faster                                                        |
| async_tree_io            | 1.07 sec                                                    | 720 ms: 1.48x faster                                                        |
| async_tree_memoization   | 497 ms                                                      | 336 ms: 1.48x faster                                                        |
| generators               | 31.6 ms                                                     | 21.5 ms: 1.47x faster                                                       |
| async_tree_none          | 420 ms                                                      | 288 ms: 1.46x faster                                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 1.01 ms: 1.46x faster                                                       |
| raytrace                 | 271 ms                                                      | 188 ms: 1.44x faster                                                        |
| hexiom                   | 5.52 ms                                                     | 3.93 ms: 1.41x faster                                                       |
| chaos                    | 58.9 ms                                                     | 43.7 ms: 1.35x faster                                                       |
| pickle_pure_python       | 257 us                                                      | 191 us: 1.34x faster                                                        |
| pyflate                  | 387 ms                                                      | 289 ms: 1.34x faster                                                        |
| mako                     | 8.80 ms                                                     | 6.61 ms: 1.33x faster                                                       |
| crypto_pyaes             | 62.3 ms                                                     | 47.1 ms: 1.32x faster                                                       |
| unpickle_pure_python     | 171 us                                                      | 131 us: 1.30x faster                                                        |
| pycparser                | 868 ms                                                      | 669 ms: 1.30x faster                                                        |
| scimark_sor              | 105 ms                                                      | 81.6 ms: 1.28x faster                                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.6 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 478 ms: 1.27x faster                                                        |
| deepcopy_memo            | 28.5 us                                                     | 23.1 us: 1.24x faster                                                       |
| tornado_http             | 109 ms                                                      | 89.5 ms: 1.22x faster                                                       |
| tomli_loads              | 1.62 sec                                                    | 1.33 sec: 1.22x faster                                                      |
| spectral_norm            | 78.0 ms                                                     | 64.3 ms: 1.21x faster                                                       |
| regex_compile            | 103 ms                                                      | 85.5 ms: 1.21x faster                                                       |
| mdp                      | 1.71 sec                                                    | 1.43 sec: 1.20x faster                                                      |
| docutils                 | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.04 sec: 1.17x faster                                                      |
| coroutines               | 15.9 ms                                                     | 13.8 ms: 1.16x faster                                                       |
| pprint_safe_repr         | 589 ms                                                      | 512 ms: 1.15x faster                                                        |
| sqlglot_optimize         | 39.0 ms                                                     | 33.9 ms: 1.15x faster                                                       |
| xml_etree_process        | 43.4 ms                                                     | 38.1 ms: 1.14x faster                                                       |
| dulwich_log              | 47.6 ms                                                     | 41.8 ms: 1.14x faster                                                       |
| comprehensions           | 16.0 us                                                     | 14.0 us: 1.14x faster                                                       |
| aiohttp                  | 1.01 ms                                                     | 891 us: 1.13x faster                                                        |
| bench_thread_pool        | 946 us                                                      | 838 us: 1.13x faster                                                        |
| unpickle                 | 9.17 us                                                     | 8.13 us: 1.13x faster                                                       |
| regex_dna                | 132 ms                                                      | 117 ms: 1.13x faster                                                        |
| 2to3                     | 237 ms                                                      | 211 ms: 1.12x faster                                                        |
| create_gc_cycles         | 782 us                                                      | 698 us: 1.12x faster                                                        |
| xml_etree_parse          | 102 ms                                                      | 91.5 ms: 1.11x faster                                                       |
| nqueens                  | 67.0 ms                                                     | 60.4 ms: 1.11x faster                                                       |
| float                    | 60.2 ms                                                     | 54.3 ms: 1.11x faster                                                       |
| sqlglot_normalize        | 202 ms                                                      | 183 ms: 1.11x faster                                                        |
| deepcopy                 | 255 us                                                      | 231 us: 1.10x faster                                                        |
| scimark_fft              | 193 ms                                                      | 178 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.46 ms: 1.08x faster                                                       |
| sqlite_synth             | 1.84 us                                                     | 1.71 us: 1.08x faster                                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.01 us: 1.07x faster                                                       |
| json_loads               | 14.2 us                                                     | 13.3 us: 1.06x faster                                                       |
| fannkuch                 | 258 ms                                                      | 245 ms: 1.05x faster                                                        |
| regex_v8                 | 15.0 ms                                                     | 14.3 ms: 1.05x faster                                                       |
| json                     | 3.05 ms                                                     | 2.92 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| python_startup           | 20.0 ms                                                     | 19.5 ms: 1.02x faster                                                       |
| meteor_contest           | 72.5 ms                                                     | 73.3 ms: 1.01x slower                                                       |
| logging_format           | 6.66 us                                                     | 6.85 us: 1.03x slower                                                       |
| pidigits                 | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| xml_etree_generate       | 54.5 ms                                                     | 56.7 ms: 1.04x slower                                                       |
| pickle                   | 6.80 us                                                     | 7.12 us: 1.05x slower                                                       |
| logging_simple           | 6.20 us                                                     | 6.52 us: 1.05x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                       |
| pathlib                  | 77.4 ms                                                     | 83.0 ms: 1.07x slower                                                       |
| telco                    | 3.78 ms                                                     | 4.08 ms: 1.08x slower                                                       |
| unpack_sequence          | 37.8 ns                                                     | 40.8 ns: 1.08x slower                                                       |
| pickle_dict              | 16.9 us                                                     | 18.6 us: 1.10x slower                                                       |
| pickle_list              | 2.59 us                                                     | 2.86 us: 1.11x slower                                                       |
| gc_traversal             | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                                       |
| bench_mp_pool            | 60.7 ms                                                     | 67.5 ms: 1.11x slower                                                       |
| dask                     | 305 ms                                                      | 364 ms: 1.19x slower                                                        |
| coverage                 | 40.0 ms                                                     | 50.3 ms: 1.26x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (5): unpickle_list, nbody, asyncio_tcp_ssl, xml_etree_iterparse, async_generators
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift

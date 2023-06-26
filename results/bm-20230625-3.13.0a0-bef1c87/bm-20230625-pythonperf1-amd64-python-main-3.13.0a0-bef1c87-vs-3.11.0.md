
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: bef1c87
- commit date: 2023-06-25
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.65 sec: 1.03x slower                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 54.6 ms                                                     | 55.5 ms: 1.02x slower                                      |
| pidigits       | 148 ms                                                      | 154 ms: 1.04x slower                                       |
| nbody          | 70.0 ms                                                     | 75.0 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 87.3 ms: 1.04x faster                                      |
| regex_v8       | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                       |
| regex_effbot   | 1.50 ms                                                     | 1.77 ms: 1.19x slower                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 6.07 ms: 1.24x faster                                      |
| unpickle_pure_python | 152 us                                                      | 136 us: 1.12x faster                                       |
| xml_etree_parse      | 95.9 ms                                                     | 93.4 ms: 1.03x faster                                      |
| pickle_pure_python   | 200 us                                                      | 197 us: 1.02x faster                                       |
| pickle_dict          | 18.5 us                                                     | 18.8 us: 1.02x slower                                      |
| tomli_loads          | 1.41 sec                                                    | 1.46 sec: 1.03x slower                                     |
| pickle_list          | 2.68 us                                                     | 2.76 us: 1.03x slower                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.9 ms: 1.04x slower                                      |
| xml_etree_process    | 37.1 ms                                                     | 38.6 ms: 1.04x slower                                      |
| unpickle             | 8.09 us                                                     | 8.61 us: 1.06x slower                                      |
| xml_etree_generate   | 52.2 ms                                                     | 55.8 ms: 1.07x slower                                      |
| pickle               | 6.61 us                                                     | 7.14 us: 1.08x slower                                      |
| json_loads           | 12.9 us                                                     | 14.4 us: 1.12x slower                                      |
| unpickle_list        | 2.55 us                                                     | 2.89 us: 1.13x slower                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 20.3 ms: 1.08x slower                                      |
| python_startup_no_site | 15.9 ms                                                     | 17.7 ms: 1.11x slower                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.43 ms: 1.02x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf1-amd64-python-main-3.13.0a0-bef1c87 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 93.7 us: 3.43x faster                                      |
| generators               | 33.8 ms                                                     | 22.9 ms: 1.48x faster                                      |
| asyncio_tcp              | 699 ms                                                      | 490 ms: 1.43x faster                                       |
| richards_super           | 37.5 ms                                                     | 29.7 ms: 1.26x faster                                      |
| json_dumps               | 7.56 ms                                                     | 6.07 ms: 1.24x faster                                      |
| raytrace                 | 211 ms                                                      | 170 ms: 1.24x faster                                       |
| deltablue                | 2.61 ms                                                     | 2.12 ms: 1.23x faster                                      |
| unpack_sequence          | 46.1 ns                                                     | 38.5 ns: 1.20x faster                                      |
| richards                 | 30.6 ms                                                     | 26.0 ms: 1.18x faster                                      |
| chaos                    | 47.1 ms                                                     | 40.4 ms: 1.17x faster                                      |
| sqlglot_parse            | 952 us                                                      | 828 us: 1.15x faster                                       |
| mdp                      | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                     |
| logging_silent           | 69.8 ns                                                     | 61.3 ns: 1.14x faster                                      |
| sqlglot_transpile        | 1.16 ms                                                     | 1.04 ms: 1.12x faster                                      |
| unpickle_pure_python     | 152 us                                                      | 136 us: 1.12x faster                                       |
| comprehensions           | 15.9 us                                                     | 14.3 us: 1.12x faster                                      |
| hexiom                   | 4.55 ms                                                     | 4.09 ms: 1.11x faster                                      |
| async_tree_memoization   | 371 ms                                                      | 341 ms: 1.09x faster                                       |
| async_tree_none          | 320 ms                                                      | 297 ms: 1.08x faster                                       |
| nqueens                  | 64.9 ms                                                     | 60.3 ms: 1.08x faster                                      |
| json                     | 3.25 ms                                                     | 3.04 ms: 1.07x faster                                      |
| coverage                 | 55.9 ms                                                     | 52.2 ms: 1.07x faster                                      |
| scimark_lu               | 63.5 ms                                                     | 60.1 ms: 1.06x faster                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.01 sec: 1.05x faster                                     |
| async_tree_io            | 779 ms                                                      | 741 ms: 1.05x faster                                       |
| mypy2                    | 229 ms                                                      | 219 ms: 1.04x faster                                       |
| deepcopy_memo            | 25.2 us                                                     | 24.2 us: 1.04x faster                                      |
| go                       | 97.3 ms                                                     | 93.6 ms: 1.04x faster                                      |
| regex_compile            | 90.6 ms                                                     | 87.3 ms: 1.04x faster                                      |
| xml_etree_parse          | 95.9 ms                                                     | 93.4 ms: 1.03x faster                                      |
| sqlglot_normalize        | 190 ms                                                      | 185 ms: 1.03x faster                                       |
| deepcopy                 | 246 us                                                      | 240 us: 1.02x faster                                       |
| logging_simple           | 6.61 us                                                     | 6.49 us: 1.02x faster                                      |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 493 ms: 1.02x faster                                       |
| pickle_pure_python       | 200 us                                                      | 197 us: 1.02x faster                                       |
| regex_v8                 | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                      |
| logging_format           | 7.01 us                                                     | 6.95 us: 1.01x faster                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 34.6 ms: 1.01x faster                                      |
| deepcopy_reduce          | 2.07 us                                                     | 2.10 us: 1.01x slower                                      |
| float                    | 54.6 ms                                                     | 55.5 ms: 1.02x slower                                      |
| crypto_pyaes             | 47.6 ms                                                     | 48.4 ms: 1.02x slower                                      |
| pickle_dict              | 18.5 us                                                     | 18.8 us: 1.02x slower                                      |
| pyflate                  | 304 ms                                                      | 310 ms: 1.02x slower                                       |
| bench_thread_pool        | 852 us                                                      | 870 us: 1.02x slower                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.62 ms: 1.02x slower                                      |
| mako                     | 7.26 ms                                                     | 7.43 ms: 1.02x slower                                      |
| scimark_monte_carlo      | 44.6 ms                                                     | 45.6 ms: 1.02x slower                                      |
| pprint_safe_repr         | 512 ms                                                      | 523 ms: 1.02x slower                                       |
| telco                    | 3.90 ms                                                     | 4.01 ms: 1.03x slower                                      |
| tomli_loads              | 1.41 sec                                                    | 1.46 sec: 1.03x slower                                     |
| pprint_pformat           | 1.04 sec                                                    | 1.07 sec: 1.03x slower                                     |
| pickle_list              | 2.68 us                                                     | 2.76 us: 1.03x slower                                      |
| docutils                 | 1.60 sec                                                    | 1.65 sec: 1.03x slower                                     |
| coroutines               | 14.6 ms                                                     | 15.1 ms: 1.03x slower                                      |
| spectral_norm            | 67.9 ms                                                     | 70.2 ms: 1.03x slower                                      |
| sqlite_synth             | 1.68 us                                                     | 1.74 us: 1.04x slower                                      |
| pidigits                 | 148 ms                                                      | 154 ms: 1.04x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.9 ms: 1.04x slower                                      |
| dulwich_log              | 44.5 ms                                                     | 46.3 ms: 1.04x slower                                      |
| xml_etree_process        | 37.1 ms                                                     | 38.6 ms: 1.04x slower                                      |
| regex_dna                | 115 ms                                                      | 120 ms: 1.04x slower                                       |
| gc_traversal             | 1.46 ms                                                     | 1.53 ms: 1.05x slower                                      |
| pycparser                | 691 ms                                                      | 726 ms: 1.05x slower                                       |
| scimark_fft              | 178 ms                                                      | 189 ms: 1.06x slower                                       |
| unpickle                 | 8.09 us                                                     | 8.61 us: 1.06x slower                                      |
| xml_etree_generate       | 52.2 ms                                                     | 55.8 ms: 1.07x slower                                      |
| nbody                    | 70.0 ms                                                     | 75.0 ms: 1.07x slower                                      |
| pickle                   | 6.61 us                                                     | 7.14 us: 1.08x slower                                      |
| create_gc_cycles         | 693 us                                                      | 748 us: 1.08x slower                                       |
| python_startup           | 18.7 ms                                                     | 20.3 ms: 1.08x slower                                      |
| bench_mp_pool            | 62.5 ms                                                     | 67.9 ms: 1.09x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 82.7 ms: 1.09x slower                                      |
| python_startup_no_site   | 15.9 ms                                                     | 17.7 ms: 1.11x slower                                      |
| json_loads               | 12.9 us                                                     | 14.4 us: 1.12x slower                                      |
| unpickle_list            | 2.55 us                                                     | 2.89 us: 1.13x slower                                      |
| pathlib                  | 71.4 ms                                                     | 83.3 ms: 1.17x slower                                      |
| regex_effbot             | 1.50 ms                                                     | 1.77 ms: 1.19x slower                                      |
| async_generators         | 178 ms                                                      | 242 ms: 1.36x slower                                       |
| Geometric mean           | (ref)                                                       | 1.03x faster                                               |

Benchmark hidden because not significant (3): tornado_http, fannkuch, meteor_contest
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift

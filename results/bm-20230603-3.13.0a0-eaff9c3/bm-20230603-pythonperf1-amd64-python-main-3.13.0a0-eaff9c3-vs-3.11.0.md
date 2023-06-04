
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: eaff9c3
- commit date: 2023-06-03
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                     |
| tornado_http   | 91.8 ms                                                     | 90.7 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 54.6 ms                                                     | 54.1 ms: 1.01x faster                                      |
| nbody          | 70.0 ms                                                     | 69.4 ms: 1.01x faster                                      |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 87.5 ms: 1.04x faster                                      |
| regex_dna      | 115 ms                                                      | 127 ms: 1.10x slower                                       |
| regex_effbot   | 1.50 ms                                                     | 1.70 ms: 1.14x slower                                      |
| regex_v8       | 13.8 ms                                                     | 24.5 ms: 1.77x slower                                      |
| Geometric mean | (ref)                                                       | 1.21x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.84 ms: 1.30x faster                                      |
| unpickle_pure_python | 152 us                                                      | 134 us: 1.14x faster                                       |
| pickle_pure_python   | 200 us                                                      | 191 us: 1.05x faster                                       |
| tomli_loads          | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                     |
| xml_etree_parse      | 95.9 ms                                                     | 94.0 ms: 1.02x faster                                      |
| xml_etree_process    | 37.1 ms                                                     | 37.7 ms: 1.02x slower                                      |
| unpickle             | 8.09 us                                                     | 8.29 us: 1.02x slower                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.0 ms: 1.04x slower                                      |
| xml_etree_generate   | 52.2 ms                                                     | 54.9 ms: 1.05x slower                                      |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                      |
| pickle_list          | 2.68 us                                                     | 2.86 us: 1.07x slower                                      |
| pickle               | 6.61 us                                                     | 7.28 us: 1.10x slower                                      |
| unpickle_list        | 2.55 us                                                     | 2.88 us: 1.13x slower                                      |
| Geometric mean       | (ref)                                                       | 1.00x slower                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.2 ms: 1.02x slower                                      |
| python_startup         | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.69 ms: 1.09x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf1-amd64-python-main-3.13.0a0-eaff9c3 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 95.1 us: 3.38x faster                                      |
| generators               | 33.8 ms                                                     | 21.4 ms: 1.58x faster                                      |
| json_dumps               | 7.56 ms                                                     | 5.84 ms: 1.30x faster                                      |
| richards_super           | 37.5 ms                                                     | 29.2 ms: 1.28x faster                                      |
| deltablue                | 2.61 ms                                                     | 2.12 ms: 1.23x faster                                      |
| richards                 | 30.6 ms                                                     | 25.6 ms: 1.19x faster                                      |
| asyncio_tcp              | 699 ms                                                      | 592 ms: 1.18x faster                                       |
| unpack_sequence          | 46.1 ns                                                     | 39.1 ns: 1.18x faster                                      |
| sqlglot_parse            | 952 us                                                      | 813 us: 1.17x faster                                       |
| logging_silent           | 69.8 ns                                                     | 59.9 ns: 1.17x faster                                      |
| unpickle_pure_python     | 152 us                                                      | 134 us: 1.14x faster                                       |
| hexiom                   | 4.55 ms                                                     | 4.03 ms: 1.13x faster                                      |
| sqlglot_transpile        | 1.16 ms                                                     | 1.03 ms: 1.13x faster                                      |
| json                     | 3.25 ms                                                     | 2.90 ms: 1.12x faster                                      |
| raytrace                 | 211 ms                                                      | 189 ms: 1.11x faster                                       |
| async_tree_none          | 320 ms                                                      | 289 ms: 1.11x faster                                       |
| go                       | 97.3 ms                                                     | 88.3 ms: 1.10x faster                                      |
| mdp                      | 1.67 sec                                                    | 1.51 sec: 1.10x faster                                     |
| chaos                    | 47.1 ms                                                     | 42.8 ms: 1.10x faster                                      |
| scimark_lu               | 63.5 ms                                                     | 57.7 ms: 1.10x faster                                      |
| mako                     | 7.26 ms                                                     | 6.69 ms: 1.09x faster                                      |
| async_tree_memoization   | 371 ms                                                      | 343 ms: 1.08x faster                                       |
| spectral_norm            | 67.9 ms                                                     | 63.2 ms: 1.08x faster                                      |
| nqueens                  | 64.9 ms                                                     | 60.4 ms: 1.07x faster                                      |
| coverage                 | 55.9 ms                                                     | 52.0 ms: 1.07x faster                                      |
| async_tree_io            | 779 ms                                                      | 731 ms: 1.07x faster                                       |
| comprehensions           | 15.9 us                                                     | 14.9 us: 1.07x faster                                      |
| mypy2                    | 229 ms                                                      | 216 ms: 1.06x faster                                       |
| pyflate                  | 304 ms                                                      | 287 ms: 1.06x faster                                       |
| fannkuch                 | 252 ms                                                      | 240 ms: 1.05x faster                                       |
| pickle_pure_python       | 200 us                                                      | 191 us: 1.05x faster                                       |
| coroutines               | 14.6 ms                                                     | 14.1 ms: 1.04x faster                                      |
| logging_simple           | 6.61 us                                                     | 6.37 us: 1.04x faster                                      |
| regex_compile            | 90.6 ms                                                     | 87.5 ms: 1.04x faster                                      |
| tomli_loads              | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                     |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 486 ms: 1.03x faster                                       |
| scimark_monte_carlo      | 44.6 ms                                                     | 43.3 ms: 1.03x faster                                      |
| deepcopy                 | 246 us                                                      | 238 us: 1.03x faster                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 33.9 ms: 1.03x faster                                      |
| sqlglot_normalize        | 190 ms                                                      | 185 ms: 1.03x faster                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.50 ms: 1.03x faster                                      |
| deepcopy_memo            | 25.2 us                                                     | 24.6 us: 1.02x faster                                      |
| logging_format           | 7.01 us                                                     | 6.87 us: 1.02x faster                                      |
| xml_etree_parse          | 95.9 ms                                                     | 94.0 ms: 1.02x faster                                      |
| tornado_http             | 91.8 ms                                                     | 90.7 ms: 1.01x faster                                      |
| pprint_pformat           | 1.04 sec                                                    | 1.03 sec: 1.01x faster                                     |
| float                    | 54.6 ms                                                     | 54.1 ms: 1.01x faster                                      |
| nbody                    | 70.0 ms                                                     | 69.4 ms: 1.01x faster                                      |
| pprint_safe_repr         | 512 ms                                                      | 509 ms: 1.01x faster                                       |
| crypto_pyaes             | 47.6 ms                                                     | 48.0 ms: 1.01x slower                                      |
| dulwich_log              | 44.5 ms                                                     | 45.0 ms: 1.01x slower                                      |
| gc_traversal             | 1.46 ms                                                     | 1.48 ms: 1.01x slower                                      |
| deepcopy_reduce          | 2.07 us                                                     | 2.11 us: 1.02x slower                                      |
| pidigits                 | 148 ms                                                      | 151 ms: 1.02x slower                                       |
| meteor_contest           | 74.7 ms                                                     | 76.1 ms: 1.02x slower                                      |
| python_startup_no_site   | 15.9 ms                                                     | 16.2 ms: 1.02x slower                                      |
| xml_etree_process        | 37.1 ms                                                     | 37.7 ms: 1.02x slower                                      |
| unpickle                 | 8.09 us                                                     | 8.29 us: 1.02x slower                                      |
| create_gc_cycles         | 693 us                                                      | 711 us: 1.03x slower                                       |
| python_startup           | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                      |
| scimark_fft              | 178 ms                                                      | 184 ms: 1.03x slower                                       |
| sqlite_synth             | 1.68 us                                                     | 1.74 us: 1.04x slower                                      |
| xml_etree_iterparse      | 62.6 ms                                                     | 65.0 ms: 1.04x slower                                      |
| docutils                 | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                     |
| telco                    | 3.90 ms                                                     | 4.07 ms: 1.04x slower                                      |
| xml_etree_generate       | 52.2 ms                                                     | 54.9 ms: 1.05x slower                                      |
| json_loads               | 12.9 us                                                     | 13.7 us: 1.06x slower                                      |
| pickle_list              | 2.68 us                                                     | 2.86 us: 1.07x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 81.1 ms: 1.07x slower                                      |
| bench_mp_pool            | 62.5 ms                                                     | 68.7 ms: 1.10x slower                                      |
| pickle                   | 6.61 us                                                     | 7.28 us: 1.10x slower                                      |
| regex_dna                | 115 ms                                                      | 127 ms: 1.10x slower                                       |
| unpickle_list            | 2.55 us                                                     | 2.88 us: 1.13x slower                                      |
| regex_effbot             | 1.50 ms                                                     | 1.70 ms: 1.14x slower                                      |
| pathlib                  | 71.4 ms                                                     | 87.2 ms: 1.22x slower                                      |
| async_generators         | 178 ms                                                      | 241 ms: 1.36x slower                                       |
| regex_v8                 | 13.8 ms                                                     | 24.5 ms: 1.77x slower                                      |
| Geometric mean           | (ref)                                                       | 1.04x faster                                               |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, bench_thread_pool, pycparser, pickle_dict
Ignored benchmarks (17) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift

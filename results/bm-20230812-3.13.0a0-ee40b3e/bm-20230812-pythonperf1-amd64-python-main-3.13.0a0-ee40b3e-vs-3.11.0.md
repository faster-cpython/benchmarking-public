
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: ee40b3e
- commit date: 2023-08-12
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.65 sec: 1.03x slower                                     |
| tornado_http   | 91.8 ms                                                     | 89.0 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                       |
| float          | 54.6 ms                                                     | 55.8 ms: 1.02x slower                                      |
| nbody          | 70.0 ms                                                     | 78.2 ms: 1.12x slower                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 93.8 ms: 1.03x slower                                      |
| regex_dna      | 115 ms                                                      | 122 ms: 1.05x slower                                       |
| regex_effbot   | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.70 ms: 1.33x faster                                      |
| unpickle_pure_python | 152 us                                                      | 145 us: 1.05x faster                                       |
| xml_etree_parse      | 95.9 ms                                                     | 91.8 ms: 1.04x faster                                      |
| pickle_pure_python   | 200 us                                                      | 198 us: 1.01x faster                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.0 ms: 1.04x slower                                      |
| json_loads           | 12.9 us                                                     | 13.6 us: 1.05x slower                                      |
| xml_etree_process    | 37.1 ms                                                     | 39.5 ms: 1.06x slower                                      |
| unpickle             | 8.09 us                                                     | 8.63 us: 1.07x slower                                      |
| pickle_list          | 2.68 us                                                     | 2.87 us: 1.07x slower                                      |
| xml_etree_generate   | 52.2 ms                                                     | 56.4 ms: 1.08x slower                                      |
| tomli_loads          | 1.41 sec                                                    | 1.54 sec: 1.09x slower                                     |
| pickle               | 6.61 us                                                     | 7.30 us: 1.11x slower                                      |
| unpickle_list        | 2.55 us                                                     | 2.82 us: 1.11x slower                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                      |
| python_startup         | 18.7 ms                                                     | 19.6 ms: 1.05x slower                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.57 ms: 1.04x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 99.2 us: 3.24x faster                                      |
| asyncio_tcp              | 699 ms                                                      | 474 ms: 1.47x faster                                       |
| generators               | 33.8 ms                                                     | 24.8 ms: 1.36x faster                                      |
| json_dumps               | 7.56 ms                                                     | 5.70 ms: 1.33x faster                                      |
| coverage                 | 55.9 ms                                                     | 45.9 ms: 1.22x faster                                      |
| raytrace                 | 211 ms                                                      | 181 ms: 1.16x faster                                       |
| async_tree_none          | 320 ms                                                      | 278 ms: 1.15x faster                                       |
| json                     | 3.25 ms                                                     | 2.85 ms: 1.14x faster                                      |
| deltablue                | 2.61 ms                                                     | 2.29 ms: 1.14x faster                                      |
| mdp                      | 1.67 sec                                                    | 1.50 sec: 1.11x faster                                     |
| sqlglot_parse            | 952 us                                                      | 863 us: 1.10x faster                                       |
| richards_super           | 37.5 ms                                                     | 34.6 ms: 1.08x faster                                      |
| unpack_sequence          | 46.1 ns                                                     | 42.6 ns: 1.08x faster                                      |
| logging_silent           | 69.8 ns                                                     | 64.7 ns: 1.08x faster                                      |
| chaos                    | 47.1 ms                                                     | 43.8 ms: 1.08x faster                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.96 sec: 1.08x faster                                     |
| sqlglot_transpile        | 1.16 ms                                                     | 1.09 ms: 1.07x faster                                      |
| scimark_lu               | 63.5 ms                                                     | 59.4 ms: 1.07x faster                                      |
| comprehensions           | 15.9 us                                                     | 15.0 us: 1.06x faster                                      |
| async_tree_io            | 779 ms                                                      | 739 ms: 1.05x faster                                       |
| unpickle_pure_python     | 152 us                                                      | 145 us: 1.05x faster                                       |
| xml_etree_parse          | 95.9 ms                                                     | 91.8 ms: 1.04x faster                                      |
| async_tree_memoization   | 371 ms                                                      | 356 ms: 1.04x faster                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 482 ms: 1.04x faster                                       |
| crypto_pyaes             | 47.6 ms                                                     | 46.0 ms: 1.03x faster                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.49 ms: 1.03x faster                                      |
| tornado_http             | 91.8 ms                                                     | 89.0 ms: 1.03x faster                                      |
| hexiom                   | 4.55 ms                                                     | 4.44 ms: 1.03x faster                                      |
| bench_thread_pool        | 852 us                                                      | 835 us: 1.02x faster                                       |
| nqueens                  | 64.9 ms                                                     | 64.0 ms: 1.01x faster                                      |
| richards                 | 30.6 ms                                                     | 30.2 ms: 1.01x faster                                      |
| meteor_contest           | 74.7 ms                                                     | 74.0 ms: 1.01x faster                                      |
| pickle_pure_python       | 200 us                                                      | 198 us: 1.01x faster                                       |
| logging_simple           | 6.61 us                                                     | 6.66 us: 1.01x slower                                      |
| go                       | 97.3 ms                                                     | 98.2 ms: 1.01x slower                                      |
| deepcopy_memo            | 25.2 us                                                     | 25.4 us: 1.01x slower                                      |
| sqlglot_normalize        | 190 ms                                                      | 193 ms: 1.01x slower                                       |
| pidigits                 | 148 ms                                                      | 151 ms: 1.02x slower                                       |
| scimark_fft              | 178 ms                                                      | 182 ms: 1.02x slower                                       |
| scimark_monte_carlo      | 44.6 ms                                                     | 45.6 ms: 1.02x slower                                      |
| float                    | 54.6 ms                                                     | 55.8 ms: 1.02x slower                                      |
| dulwich_log              | 44.5 ms                                                     | 45.5 ms: 1.02x slower                                      |
| logging_format           | 7.01 us                                                     | 7.18 us: 1.02x slower                                      |
| gc_traversal             | 1.46 ms                                                     | 1.50 ms: 1.03x slower                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 35.8 ms: 1.03x slower                                      |
| docutils                 | 1.60 sec                                                    | 1.65 sec: 1.03x slower                                     |
| python_startup_no_site   | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                      |
| pyflate                  | 304 ms                                                      | 315 ms: 1.03x slower                                       |
| regex_compile            | 90.6 ms                                                     | 93.8 ms: 1.03x slower                                      |
| deepcopy                 | 246 us                                                      | 254 us: 1.04x slower                                       |
| sqlite_synth             | 1.68 us                                                     | 1.74 us: 1.04x slower                                      |
| xml_etree_iterparse      | 62.6 ms                                                     | 65.0 ms: 1.04x slower                                      |
| pprint_safe_repr         | 512 ms                                                      | 533 ms: 1.04x slower                                       |
| mako                     | 7.26 ms                                                     | 7.57 ms: 1.04x slower                                      |
| fannkuch                 | 252 ms                                                      | 264 ms: 1.05x slower                                       |
| coroutines               | 14.6 ms                                                     | 15.3 ms: 1.05x slower                                      |
| python_startup           | 18.7 ms                                                     | 19.6 ms: 1.05x slower                                      |
| pprint_pformat           | 1.04 sec                                                    | 1.09 sec: 1.05x slower                                     |
| json_loads               | 12.9 us                                                     | 13.6 us: 1.05x slower                                      |
| create_gc_cycles         | 693 us                                                      | 729 us: 1.05x slower                                       |
| regex_dna                | 115 ms                                                      | 122 ms: 1.05x slower                                       |
| bench_mp_pool            | 62.5 ms                                                     | 66.1 ms: 1.06x slower                                      |
| xml_etree_process        | 37.1 ms                                                     | 39.5 ms: 1.06x slower                                      |
| unpickle                 | 8.09 us                                                     | 8.63 us: 1.07x slower                                      |
| pickle_list              | 2.68 us                                                     | 2.87 us: 1.07x slower                                      |
| regex_effbot             | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                      |
| pycparser                | 691 ms                                                      | 743 ms: 1.08x slower                                       |
| xml_etree_generate       | 52.2 ms                                                     | 56.4 ms: 1.08x slower                                      |
| tomli_loads              | 1.41 sec                                                    | 1.54 sec: 1.09x slower                                     |
| deepcopy_reduce          | 2.07 us                                                     | 2.26 us: 1.09x slower                                      |
| pathlib                  | 71.4 ms                                                     | 78.5 ms: 1.10x slower                                      |
| pickle                   | 6.61 us                                                     | 7.30 us: 1.11x slower                                      |
| unpickle_list            | 2.55 us                                                     | 2.82 us: 1.11x slower                                      |
| nbody                    | 70.0 ms                                                     | 78.2 ms: 1.12x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 84.9 ms: 1.12x slower                                      |
| telco                    | 3.90 ms                                                     | 4.74 ms: 1.21x slower                                      |
| mypy2                    | 229 ms                                                      | 302 ms: 1.32x slower                                       |
| async_generators         | 178 ms                                                      | 245 ms: 1.38x slower                                       |
| dask                     | 264 ms                                                      | 383 ms: 1.45x slower                                       |
| Geometric mean           | (ref)                                                       | 1.01x faster                                               |

Benchmark hidden because not significant (3): pickle_dict, regex_v8, spectral_norm
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift

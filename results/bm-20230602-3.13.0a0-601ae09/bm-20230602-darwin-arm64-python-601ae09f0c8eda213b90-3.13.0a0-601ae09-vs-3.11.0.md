
# Results vs. 3.11.0

- fork: python
- ref: 601ae09f0c8eda213b90
- machine: darwin-arm64
- commit hash: 601ae09
- commit date: 2023-06-02
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.51 sec: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| nbody          | 65.6 ms                                                | 69.0 ms: 1.05x slower                                                 |
| float          | 53.0 ms                                                | 57.1 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.6 ms: 1.03x faster                                                 |
| regex_compile  | 76.7 ms                                                | 75.4 ms: 1.02x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.33 ms: 1.21x faster                                                 |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.10x faster                                                  |
| tomli_loads          | 1.47 sec                                               | 1.39 sec: 1.06x faster                                                |
| pickle_pure_python   | 201 us                                                 | 190 us: 1.05x faster                                                  |
| unpickle             | 9.67 us                                                | 9.27 us: 1.04x faster                                                 |
| pickle_dict          | 18.0 us                                                | 18.2 us: 1.01x slower                                                 |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.87 us: 1.02x slower                                                 |
| pickle               | 7.15 us                                                | 7.42 us: 1.04x slower                                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 75.1 ms: 1.07x slower                                                 |
| json_loads           | 16.1 us                                                | 17.5 us: 1.09x slower                                                 |
| xml_etree_process    | 35.1 ms                                                | 39.0 ms: 1.11x slower                                                 |
| xml_etree_generate   | 48.3 ms                                                | 56.2 ms: 1.16x slower                                                 |
| unpickle_list        | 2.65 us                                                | 3.19 us: 1.21x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.54 ms: 1.13x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 89.3 us: 3.76x faster                                                 |
| asyncio_tcp              | 651 ms                                                 | 444 ms: 1.47x faster                                                  |
| json_dumps               | 7.63 ms                                                | 6.33 ms: 1.21x faster                                                 |
| unpack_sequence          | 34.1 ns                                                | 28.3 ns: 1.20x faster                                                 |
| chaos                    | 49.4 ms                                                | 41.9 ms: 1.18x faster                                                 |
| deltablue                | 2.81 ms                                                | 2.40 ms: 1.17x faster                                                 |
| sqlglot_parse            | 959 us                                                 | 829 us: 1.16x faster                                                  |
| go                       | 109 ms                                                 | 94.0 ms: 1.16x faster                                                 |
| coverage                 | 58.4 ms                                                | 50.8 ms: 1.15x faster                                                 |
| richards_super           | 39.2 ms                                                | 34.1 ms: 1.15x faster                                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.26 sec: 1.15x faster                                                |
| mako                     | 8.53 ms                                                | 7.54 ms: 1.13x faster                                                 |
| sqlglot_transpile        | 1.12 ms                                                | 1.00 ms: 1.12x faster                                                 |
| hexiom                   | 4.72 ms                                                | 4.23 ms: 1.12x faster                                                 |
| unpickle_pure_python     | 159 us                                                 | 145 us: 1.10x faster                                                  |
| comprehensions           | 16.1 us                                                | 14.9 us: 1.08x faster                                                 |
| generators               | 28.8 ms                                                | 26.7 ms: 1.08x faster                                                 |
| scimark_monte_carlo      | 46.5 ms                                                | 43.2 ms: 1.08x faster                                                 |
| richards                 | 32.2 ms                                                | 30.2 ms: 1.07x faster                                                 |
| tomli_loads              | 1.47 sec                                               | 1.39 sec: 1.06x faster                                                |
| pickle_pure_python       | 201 us                                                 | 190 us: 1.05x faster                                                  |
| deepcopy_memo            | 26.3 us                                                | 25.0 us: 1.05x faster                                                 |
| unpickle                 | 9.67 us                                                | 9.27 us: 1.04x faster                                                 |
| pycparser                | 698 ms                                                 | 672 ms: 1.04x faster                                                  |
| regex_v8                 | 16.1 ms                                                | 15.6 ms: 1.03x faster                                                 |
| create_gc_cycles         | 716 us                                                 | 697 us: 1.03x faster                                                  |
| async_tree_memoization   | 336 ms                                                 | 327 ms: 1.03x faster                                                  |
| regex_compile            | 76.7 ms                                                | 75.4 ms: 1.02x faster                                                 |
| async_tree_none          | 286 ms                                                 | 280 ms: 1.02x faster                                                  |
| regex_effbot             | 2.63 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_dna                | 152 ms                                                 | 150 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.15 ms: 1.01x faster                                                 |
| dulwich_log              | 30.3 ms                                                | 30.0 ms: 1.01x faster                                                 |
| python_startup           | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                 |
| scimark_lu               | 73.3 ms                                                | 72.9 ms: 1.01x faster                                                 |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                                 |
| async_tree_io            | 704 ms                                                 | 701 ms: 1.01x faster                                                  |
| meteor_contest           | 73.5 ms                                                | 73.2 ms: 1.00x faster                                                 |
| crypto_pyaes             | 51.7 ms                                                | 51.6 ms: 1.00x faster                                                 |
| scimark_fft              | 200 ms                                                 | 199 ms: 1.00x faster                                                  |
| raytrace                 | 207 ms                                                 | 207 ms: 1.00x slower                                                  |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| logging_simple           | 3.55 us                                                | 3.58 us: 1.01x slower                                                 |
| pyflate                  | 310 ms                                                 | 313 ms: 1.01x slower                                                  |
| pickle_dict              | 18.0 us                                                | 18.2 us: 1.01x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| fannkuch                 | 261 ms                                                 | 266 ms: 1.02x slower                                                  |
| bench_thread_pool        | 474 us                                                 | 483 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 543 ms: 1.02x slower                                                  |
| logging_format           | 3.78 us                                                | 3.85 us: 1.02x slower                                                 |
| pickle_list              | 2.81 us                                                | 2.87 us: 1.02x slower                                                 |
| deepcopy                 | 223 us                                                 | 227 us: 1.02x slower                                                  |
| logging_silent           | 68.1 ns                                                | 69.7 ns: 1.02x slower                                                 |
| docutils                 | 1.47 sec                                               | 1.51 sec: 1.03x slower                                                |
| spectral_norm            | 72.6 ms                                                | 74.7 ms: 1.03x slower                                                 |
| scimark_sor              | 82.6 ms                                                | 85.4 ms: 1.03x slower                                                 |
| pickle                   | 7.15 us                                                | 7.42 us: 1.04x slower                                                 |
| nbody                    | 65.6 ms                                                | 69.0 ms: 1.05x slower                                                 |
| bench_mp_pool            | 43.9 ms                                                | 46.3 ms: 1.05x slower                                                 |
| pprint_pformat           | 954 ms                                                 | 1.01 sec: 1.05x slower                                                |
| pprint_safe_repr         | 466 ms                                                 | 494 ms: 1.06x slower                                                  |
| mdp                      | 1.55 sec                                               | 1.64 sec: 1.06x slower                                                |
| xml_etree_iterparse      | 70.1 ms                                                | 75.1 ms: 1.07x slower                                                 |
| json                     | 2.78 ms                                                | 2.99 ms: 1.08x slower                                                 |
| float                    | 53.0 ms                                                | 57.1 ms: 1.08x slower                                                 |
| sqlglot_normalize        | 171 ms                                                 | 184 ms: 1.08x slower                                                  |
| deepcopy_reduce          | 1.91 us                                                | 2.06 us: 1.08x slower                                                 |
| json_loads               | 16.1 us                                                | 17.5 us: 1.09x slower                                                 |
| telco                    | 3.41 ms                                                | 3.74 ms: 1.10x slower                                                 |
| sqlglot_optimize         | 31.1 ms                                                | 34.3 ms: 1.10x slower                                                 |
| xml_etree_process        | 35.1 ms                                                | 39.0 ms: 1.11x slower                                                 |
| xml_etree_generate       | 48.3 ms                                                | 56.2 ms: 1.16x slower                                                 |
| unpickle_list            | 2.65 us                                                | 3.19 us: 1.21x slower                                                 |
| sqlite_synth             | 1.27 us                                                | 1.57 us: 1.23x slower                                                 |
| pathlib                  | 27.2 ms                                                | 33.7 ms: 1.24x slower                                                 |
| mypy2                    | 195 ms                                                 | 259 ms: 1.33x slower                                                  |
| async_generators         | 196 ms                                                 | 311 ms: 1.58x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (4): tornado_http, nqueens, coroutines, python_startup_no_site
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230602-3.13.0a0-601ae09/bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09.json: dask

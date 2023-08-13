
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: ee40b3e
- commit date: 2023-08-12
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.52 sec: 1.03x slower                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                  |
| float          | 53.0 ms                                                | 56.6 ms: 1.07x slower                                 |
| nbody          | 65.6 ms                                                | 72.4 ms: 1.10x slower                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.02x faster                                 |
| regex_effbot   | 2.63 ms                                                | 2.59 ms: 1.02x faster                                 |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                  |
| regex_compile  | 76.7 ms                                                | 78.5 ms: 1.02x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.58 ms: 1.16x faster                                 |
| unpickle             | 9.67 us                                                | 9.16 us: 1.06x faster                                 |
| pickle_pure_python   | 201 us                                                 | 200 us: 1.00x faster                                  |
| pickle_dict          | 18.0 us                                                | 17.9 us: 1.00x faster                                 |
| unpickle_pure_python | 159 us                                                 | 162 us: 1.02x slower                                  |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                  |
| pickle               | 7.15 us                                                | 7.41 us: 1.04x slower                                 |
| pickle_list          | 2.81 us                                                | 2.94 us: 1.05x slower                                 |
| tomli_loads          | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| json_loads           | 16.1 us                                                | 17.5 us: 1.09x slower                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 76.9 ms: 1.10x slower                                 |
| xml_etree_process    | 35.1 ms                                                | 40.8 ms: 1.16x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.15 us: 1.19x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 58.6 ms: 1.21x slower                                 |
| Geometric mean       | (ref)                                                  | 1.05x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.15 ms: 1.11x faster                                 |
| python_startup         | 12.4 ms                                                | 11.3 ms: 1.10x faster                                 |
| Geometric mean         | (ref)                                                  | 1.11x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.46 ms: 1.14x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 94.6 us: 3.55x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 419 ms: 1.55x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 27.5 ns: 1.24x faster                                 |
| coverage                 | 58.4 ms                                                | 47.6 ms: 1.23x faster                                 |
| chaos                    | 49.4 ms                                                | 42.3 ms: 1.17x faster                                 |
| json_dumps               | 7.63 ms                                                | 6.58 ms: 1.16x faster                                 |
| mako                     | 8.53 ms                                                | 7.46 ms: 1.14x faster                                 |
| sqlglot_parse            | 959 us                                                 | 840 us: 1.14x faster                                  |
| sqlglot_transpile        | 1.12 ms                                                | 1.01 ms: 1.12x faster                                 |
| deltablue                | 2.81 ms                                                | 2.53 ms: 1.11x faster                                 |
| python_startup_no_site   | 10.2 ms                                                | 9.15 ms: 1.11x faster                                 |
| async_tree_none          | 286 ms                                                 | 257 ms: 1.11x faster                                  |
| python_startup           | 12.4 ms                                                | 11.3 ms: 1.10x faster                                 |
| raytrace                 | 207 ms                                                 | 188 ms: 1.10x faster                                  |
| crypto_pyaes             | 51.7 ms                                                | 47.6 ms: 1.09x faster                                 |
| comprehensions           | 16.1 us                                                | 15.1 us: 1.07x faster                                 |
| unpickle                 | 9.67 us                                                | 9.16 us: 1.06x faster                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.36 sec: 1.06x faster                                |
| deepcopy_memo            | 26.3 us                                                | 25.1 us: 1.05x faster                                 |
| create_gc_cycles         | 716 us                                                 | 690 us: 1.04x faster                                  |
| generators               | 28.8 ms                                                | 28.0 ms: 1.03x faster                                 |
| regex_v8                 | 16.1 ms                                                | 15.7 ms: 1.02x faster                                 |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.14 ms: 1.02x faster                                 |
| regex_effbot             | 2.63 ms                                                | 2.59 ms: 1.02x faster                                 |
| regex_dna                | 152 ms                                                 | 150 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 528 ms: 1.01x faster                                  |
| gc_traversal             | 2.42 ms                                                | 2.39 ms: 1.01x faster                                 |
| pickle_pure_python       | 201 us                                                 | 200 us: 1.00x faster                                  |
| go                       | 109 ms                                                 | 108 ms: 1.00x faster                                  |
| pickle_dict              | 18.0 us                                                | 17.9 us: 1.00x faster                                 |
| pidigits                 | 281 ms                                                 | 281 ms: 1.00x slower                                  |
| async_tree_io            | 704 ms                                                 | 709 ms: 1.01x slower                                  |
| richards_super           | 39.2 ms                                                | 39.5 ms: 1.01x slower                                 |
| scimark_fft              | 200 ms                                                 | 202 ms: 1.01x slower                                  |
| meteor_contest           | 73.5 ms                                                | 74.6 ms: 1.02x slower                                 |
| unpickle_pure_python     | 159 us                                                 | 162 us: 1.02x slower                                  |
| regex_compile            | 76.7 ms                                                | 78.5 ms: 1.02x slower                                 |
| dulwich_log              | 30.3 ms                                                | 31.1 ms: 1.02x slower                                 |
| scimark_lu               | 73.3 ms                                                | 75.4 ms: 1.03x slower                                 |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.03x slower                                  |
| hexiom                   | 4.72 ms                                                | 4.86 ms: 1.03x slower                                 |
| bench_mp_pool            | 43.9 ms                                                | 45.3 ms: 1.03x slower                                 |
| docutils                 | 1.47 sec                                               | 1.52 sec: 1.03x slower                                |
| pickle                   | 7.15 us                                                | 7.41 us: 1.04x slower                                 |
| bench_thread_pool        | 474 us                                                 | 493 us: 1.04x slower                                  |
| spectral_norm            | 72.6 ms                                                | 75.8 ms: 1.04x slower                                 |
| pickle_list              | 2.81 us                                                | 2.94 us: 1.05x slower                                 |
| deepcopy                 | 223 us                                                 | 233 us: 1.05x slower                                  |
| mdp                      | 1.55 sec                                               | 1.64 sec: 1.06x slower                                |
| float                    | 53.0 ms                                                | 56.6 ms: 1.07x slower                                 |
| tomli_loads              | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| logging_simple           | 3.55 us                                                | 3.82 us: 1.08x slower                                 |
| logging_silent           | 68.1 ns                                                | 73.7 ns: 1.08x slower                                 |
| logging_format           | 3.78 us                                                | 4.10 us: 1.09x slower                                 |
| fannkuch                 | 261 ms                                                 | 284 ms: 1.09x slower                                  |
| json_loads               | 16.1 us                                                | 17.5 us: 1.09x slower                                 |
| json                     | 2.78 ms                                                | 3.03 ms: 1.09x slower                                 |
| coroutines               | 17.8 ms                                                | 19.5 ms: 1.10x slower                                 |
| xml_etree_iterparse      | 70.1 ms                                                | 76.9 ms: 1.10x slower                                 |
| nbody                    | 65.6 ms                                                | 72.4 ms: 1.10x slower                                 |
| deepcopy_reduce          | 1.91 us                                                | 2.11 us: 1.11x slower                                 |
| richards                 | 32.2 ms                                                | 35.9 ms: 1.11x slower                                 |
| sqlglot_normalize        | 171 ms                                                 | 191 ms: 1.12x slower                                  |
| pyflate                  | 310 ms                                                 | 348 ms: 1.12x slower                                  |
| pprint_pformat           | 954 ms                                                 | 1.07 sec: 1.12x slower                                |
| pprint_safe_repr         | 466 ms                                                 | 528 ms: 1.13x slower                                  |
| sqlglot_optimize         | 31.1 ms                                                | 35.3 ms: 1.13x slower                                 |
| pathlib                  | 27.2 ms                                                | 31.3 ms: 1.15x slower                                 |
| xml_etree_process        | 35.1 ms                                                | 40.8 ms: 1.16x slower                                 |
| unpickle_list            | 2.65 us                                                | 3.15 us: 1.19x slower                                 |
| xml_etree_generate       | 48.3 ms                                                | 58.6 ms: 1.21x slower                                 |
| sqlite_synth             | 1.27 us                                                | 1.59 us: 1.25x slower                                 |
| scimark_sor              | 82.6 ms                                                | 108 ms: 1.31x slower                                  |
| telco                    | 3.41 ms                                                | 4.53 ms: 1.33x slower                                 |
| mypy2                    | 195 ms                                                 | 261 ms: 1.34x slower                                  |
| async_generators         | 196 ms                                                 | 310 ms: 1.58x slower                                  |
| Geometric mean           | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (5): async_tree_memoization, tornado_http, nqueens, scimark_monte_carlo, pycparser
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230812-3.13.0a0-ee40b3e/bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e.json: dask

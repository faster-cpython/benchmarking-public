# Results vs. 3.12.0

- fork: eendebakpt
- ref: pycfunctionobject_fr
- machine: linux-x86_64
- commit hash: 7a165db
- commit date: 2025-01-27
- overall geometric mean: 1.106x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.07x faster                                                       |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                       |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.79x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.75x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 73.6 ms: 1.15x faster                                                      |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| nbody          | 97.0 ms                                                | 98.2 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.27 ms: 1.10x faster                                                      |
| regex_dna      | 212 ms                                                 | 209 ms: 1.01x faster                                                       |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 85.1 ms: 1.05x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                      |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                      |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.35x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                      |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                       |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.79x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.75x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                       |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 31.3 us: 1.30x faster                                                      |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                      |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                      |
| async_generators           | 463 ms                                                 | 385 ms: 1.20x faster                                                       |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                                      |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                       |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 145 ms: 1.16x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                     |
| float                      | 84.7 ms                                                | 73.6 ms: 1.15x faster                                                      |
| spectral_norm              | 115 ms                                                 | 99.8 ms: 1.15x faster                                                      |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                       |
| sympy_str                  | 300 ms                                                 | 263 ms: 1.14x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                                      |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.5 ms: 1.14x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 72.8 ms: 1.12x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.27 ms: 1.10x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 68.7 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                                      |
| generators                 | 31.2 ms                                                | 28.7 ms: 1.09x faster                                                      |
| sympy_expand               | 478 ms                                                 | 444 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.70 ms: 1.08x faster                                                      |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.08x faster                                                       |
| 2to3                       | 274 ms                                                 | 255 ms: 1.07x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                     |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.06x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 64.5 ms: 1.06x faster                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 51.6 ms: 1.06x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                      |
| scimark_fft                | 382 ms                                                 | 362 ms: 1.06x faster                                                       |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 85.1 ms: 1.05x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                       |
| nqueens                    | 83.3 ms                                                | 79.8 ms: 1.04x faster                                                      |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                      |
| richards                   | 45.8 ms                                                | 44.5 ms: 1.03x faster                                                      |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                                       |
| richards_super             | 51.5 ms                                                | 50.4 ms: 1.02x faster                                                      |
| json                       | 5.26 ms                                                | 5.16 ms: 1.02x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                     |
| hexiom                     | 6.41 ms                                                | 6.30 ms: 1.02x faster                                                      |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.01x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| pyflate                    | 482 ms                                                 | 484 ms: 1.00x slower                                                       |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                       |
| nbody                      | 97.0 ms                                                | 98.2 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 859 us: 1.02x slower                                                       |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                      |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                      |
| telco                      | 7.10 ms                                                | 7.76 ms: 1.09x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                      |
| coverage                   | 72.7 ms                                                | 91.2 ms: 1.25x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.95 ms: 1.30x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.35x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250127-3.14.0a4+-7a165db/bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.106x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.09x
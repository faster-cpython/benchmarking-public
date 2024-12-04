# Results vs. 3.12.0

- fork: python
- ref: v3.13.1
- machine: linux-x86_64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.055x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 267 ms: 1.03x faster                                   |
| chameleon      | 7.41 ms                                                | 7.09 ms: 1.04x faster                                  |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                 |
| tornado_http   | 103 ms                                                 | 91.4 ms: 1.12x faster                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.44x faster                                   |
| async_tree_io              | 1.16 sec                                               | 835 ms: 1.39x faster                                   |
| async_tree_io_tg           | 1.18 sec                                               | 857 ms: 1.38x faster                                   |
| async_tree_none            | 472 ms                                                 | 349 ms: 1.35x faster                                   |
| async_tree_memoization     | 578 ms                                                 | 447 ms: 1.29x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 452 ms: 1.27x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 576 ms: 1.26x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                   |
| Geometric mean             | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.2 ms: 1.08x faster                                  |
| nbody          | 97.0 ms                                                | 90.5 ms: 1.07x faster                                  |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                   |
| regex_effbot   | 3.61 ms                                                | 3.49 ms: 1.03x faster                                  |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                   |
| regex_v8       | 23.1 ms                                                | 26.6 ms: 1.15x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                 |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                   |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.06x faster                                   |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                   |
| json_loads           | 28.5 us                                                | 27.3 us: 1.04x faster                                  |
| xml_etree_generate   | 89.2 ms                                                | 86.2 ms: 1.03x faster                                  |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                   |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                  |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.00x faster                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.97 ms: 1.00x slower                                  |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                  |
| Geometric mean         | (ref)                                                  | 1.15x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                  |
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.44x faster                                   |
| async_tree_io              | 1.16 sec                                               | 835 ms: 1.39x faster                                   |
| async_tree_io_tg           | 1.18 sec                                               | 857 ms: 1.38x faster                                   |
| async_tree_none            | 472 ms                                                 | 349 ms: 1.35x faster                                   |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 447 ms: 1.29x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 452 ms: 1.27x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 576 ms: 1.26x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                   |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                   |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                  |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                  |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                  |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                  |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                   |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 66.9 ms: 1.12x faster                                  |
| tornado_http               | 103 ms                                                 | 91.4 ms: 1.12x faster                                  |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                   |
| pathlib                    | 19.3 ms                                                | 17.5 ms: 1.11x faster                                  |
| crypto_pyaes               | 81.9 ms                                                | 74.1 ms: 1.10x faster                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                  |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                  |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.09x faster                                   |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.08x faster                                  |
| float                      | 84.7 ms                                                | 78.2 ms: 1.08x faster                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                  |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                  |
| nbody                      | 97.0 ms                                                | 90.5 ms: 1.07x faster                                  |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                   |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                  |
| scimark_fft                | 382 ms                                                 | 359 ms: 1.06x faster                                   |
| async_generators           | 463 ms                                                 | 436 ms: 1.06x faster                                   |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                 |
| nqueens                    | 83.3 ms                                                | 78.8 ms: 1.06x faster                                  |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.06x faster                                   |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                   |
| dulwich_log                | 68.5 ms                                                | 65.0 ms: 1.05x faster                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.20 us: 1.04x faster                                  |
| chameleon                  | 7.41 ms                                                | 7.09 ms: 1.04x faster                                  |
| json_loads                 | 28.5 us                                                | 27.3 us: 1.04x faster                                  |
| deepcopy                   | 371 us                                                 | 356 us: 1.04x faster                                   |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                   |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                   |
| gunicorn                   | 1.24 ms                                                | 1.20 ms: 1.04x faster                                  |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                 |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                  |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.04x faster                                   |
| deepcopy_memo              | 40.7 us                                                | 39.3 us: 1.04x faster                                  |
| xml_etree_generate         | 89.2 ms                                                | 86.2 ms: 1.03x faster                                  |
| regex_effbot               | 3.61 ms                                                | 3.49 ms: 1.03x faster                                  |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                   |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                 |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                   |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                   |
| pyflate                    | 482 ms                                                 | 468 ms: 1.03x faster                                   |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                   |
| bench_thread_pool          | 842 us                                                 | 818 us: 1.03x faster                                   |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                  |
| 2to3                       | 274 ms                                                 | 267 ms: 1.03x faster                                   |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                   |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                   |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.02x faster                                  |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                  |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                 |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                   |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.00x faster                                  |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                   |
| python_startup_no_site     | 6.94 ms                                                | 6.97 ms: 1.00x slower                                  |
| go                         | 139 ms                                                 | 142 ms: 1.01x slower                                   |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                  |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                   |
| sqlite_synth               | 2.83 us                                                | 2.93 us: 1.04x slower                                  |
| richards                   | 45.8 ms                                                | 48.4 ms: 1.06x slower                                  |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                   |
| richards_super             | 51.5 ms                                                | 55.1 ms: 1.07x slower                                  |
| regex_v8                   | 23.1 ms                                                | 26.6 ms: 1.15x slower                                  |
| gc_traversal               | 3.79 ms                                                | 4.41 ms: 1.16x slower                                  |
| coverage                   | 72.7 ms                                                | 84.9 ms: 1.17x slower                                  |
| telco                      | 7.10 ms                                                | 8.52 ms: 1.20x slower                                  |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.43 ms: 1.65x slower                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (3): bench_mp_pool, asyncio_websockets, scimark_sparse_mat_mult
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241203-3.13.1-0671451/bm-20241203-linux-x86_64-python-v3.13.1-3.13.1-0671451.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.07x
# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.052x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 267 ms: 1.03x faster                                   |
| chameleon      | 7.41 ms                                                | 6.94 ms: 1.07x faster                                  |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                 |
| tornado_http   | 103 ms                                                 | 92.4 ms: 1.11x faster                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                   |
| async_tree_io_tg           | 1.18 sec                                               | 857 ms: 1.38x faster                                   |
| async_tree_io              | 1.16 sec                                               | 842 ms: 1.37x faster                                   |
| async_tree_none            | 472 ms                                                 | 351 ms: 1.35x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                   |
| async_tree_memoization     | 578 ms                                                 | 442 ms: 1.31x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 577 ms: 1.26x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 464 ms: 1.24x faster                                   |
| Geometric mean             | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.0 ms: 1.12x faster                                  |
| float          | 84.7 ms                                                | 79.2 ms: 1.07x faster                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                   |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                   |
| regex_effbot   | 3.61 ms                                                | 3.73 ms: 1.03x slower                                  |
| regex_v8       | 23.1 ms                                                | 26.2 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.14 sec: 1.09x faster                                 |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                   |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                   |
| json_loads           | 28.5 us                                                | 27.2 us: 1.05x faster                                  |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.04x faster                                   |
| xml_etree_generate   | 89.2 ms                                                | 86.7 ms: 1.03x faster                                  |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                   |
| xml_etree_process    | 61.7 ms                                                | 60.6 ms: 1.02x faster                                  |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                  |
| python_startup         | 9.55 ms                                                | 12.5 ms: 1.31x slower                                  |
| Geometric mean         | (ref)                                                  | 1.14x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                  |
| django_template | 34.6 ms                                                | 35.2 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                   |
| async_tree_io_tg           | 1.18 sec                                               | 857 ms: 1.38x faster                                   |
| async_tree_io              | 1.16 sec                                               | 842 ms: 1.37x faster                                   |
| async_tree_none            | 472 ms                                                 | 351 ms: 1.35x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                   |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 442 ms: 1.31x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 577 ms: 1.26x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 464 ms: 1.24x faster                                   |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                   |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                  |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                  |
| logging_format             | 7.23 us                                                | 6.40 us: 1.13x faster                                  |
| logging_simple             | 6.46 us                                                | 5.72 us: 1.13x faster                                  |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                   |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                   |
| nbody                      | 97.0 ms                                                | 87.0 ms: 1.12x faster                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                  |
| tornado_http               | 103 ms                                                 | 92.4 ms: 1.11x faster                                  |
| pathlib                    | 19.3 ms                                                | 17.5 ms: 1.10x faster                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                  |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                   |
| tomli_loads                | 2.33 sec                                               | 2.14 sec: 1.09x faster                                 |
| crypto_pyaes               | 81.9 ms                                                | 75.3 ms: 1.09x faster                                  |
| generators                 | 31.2 ms                                                | 29.0 ms: 1.08x faster                                  |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                  |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                  |
| float                      | 84.7 ms                                                | 79.2 ms: 1.07x faster                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                  |
| chameleon                  | 7.41 ms                                                | 6.94 ms: 1.07x faster                                  |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                 |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                   |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.07x faster                                   |
| dulwich_log                | 68.5 ms                                                | 64.3 ms: 1.06x faster                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                  |
| nqueens                    | 83.3 ms                                                | 78.4 ms: 1.06x faster                                  |
| async_generators           | 463 ms                                                 | 436 ms: 1.06x faster                                   |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                   |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                 |
| scimark_fft                | 382 ms                                                 | 364 ms: 1.05x faster                                   |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                   |
| json_loads                 | 28.5 us                                                | 27.2 us: 1.05x faster                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.20 us: 1.05x faster                                  |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.05x faster                                   |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.04x faster                                   |
| deepcopy_memo              | 40.7 us                                                | 39.1 us: 1.04x faster                                  |
| hexiom                     | 6.41 ms                                                | 6.16 ms: 1.04x faster                                  |
| deepcopy                   | 371 us                                                 | 358 us: 1.04x faster                                   |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                   |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                   |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                   |
| 2to3                       | 274 ms                                                 | 267 ms: 1.03x faster                                   |
| xml_etree_generate         | 89.2 ms                                                | 86.7 ms: 1.03x faster                                  |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                   |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                   |
| bench_thread_pool          | 842 us                                                 | 822 us: 1.02x faster                                   |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                   |
| pyflate                    | 482 ms                                                 | 471 ms: 1.02x faster                                   |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                  |
| xml_etree_process          | 61.7 ms                                                | 60.6 ms: 1.02x faster                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                   |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                  |
| django_template            | 34.6 ms                                                | 35.2 ms: 1.02x slower                                  |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                  |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                  |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                 |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                   |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                   |
| regex_effbot               | 3.61 ms                                                | 3.73 ms: 1.03x slower                                  |
| mdp                        | 2.63 sec                                               | 2.72 sec: 1.03x slower                                 |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                   |
| richards                   | 45.8 ms                                                | 48.7 ms: 1.06x slower                                  |
| richards_super             | 51.5 ms                                                | 54.9 ms: 1.06x slower                                  |
| regex_v8                   | 23.1 ms                                                | 26.2 ms: 1.13x slower                                  |
| gc_traversal               | 3.79 ms                                                | 4.37 ms: 1.15x slower                                  |
| coverage                   | 72.7 ms                                                | 84.0 ms: 1.16x slower                                  |
| telco                      | 7.10 ms                                                | 8.54 ms: 1.20x slower                                  |
| mypy2                      | 830 ms                                                 | 1.04 sec: 1.26x slower                                 |
| python_startup             | 9.55 ms                                                | 12.5 ms: 1.31x slower                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.41 ms: 1.63x slower                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (4): scimark_sparse_mat_mult, bench_mp_pool, asyncio_websockets, spectral_norm
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.052x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.07x
# Results vs. 3.13.0

- fork: python
- ref: v3.12.0
- machine: linux-x86_64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.047x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 274 ms: 1.03x slower                                   |
| chameleon      | 6.94 ms                                                | 7.41 ms: 1.07x slower                                  |
| docutils       | 2.59 sec                                               | 2.77 sec: 1.07x slower                                 |
| tornado_http   | 92.4 ms                                                | 103 ms: 1.11x slower                                   |
| Geometric mean | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                  |
| async_generators           | 436 ms                                                 | 463 ms: 1.06x slower                                   |
| async_tree_memoization_tg  | 464 ms                                                 | 575 ms: 1.24x slower                                   |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 726 ms: 1.26x slower                                   |
| async_tree_memoization     | 442 ms                                                 | 578 ms: 1.31x slower                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 726 ms: 1.33x slower                                   |
| async_tree_none            | 351 ms                                                 | 472 ms: 1.35x slower                                   |
| async_tree_io              | 842 ms                                                 | 1.16 sec: 1.37x slower                                 |
| async_tree_io_tg           | 857 ms                                                 | 1.18 sec: 1.38x slower                                 |
| async_tree_none_tg         | 321 ms                                                 | 450 ms: 1.40x slower                                   |
| Geometric mean             | (ref)                                                  | 1.24x slower                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                   |
| float          | 79.2 ms                                                | 84.7 ms: 1.07x slower                                  |
| nbody          | 87.0 ms                                                | 97.0 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 23.1 ms: 1.13x faster                                  |
| regex_effbot   | 3.73 ms                                                | 3.61 ms: 1.03x faster                                  |
| regex_dna      | 218 ms                                                 | 212 ms: 1.03x faster                                   |
| regex_compile  | 132 ms                                                 | 148 ms: 1.12x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.02x faster                                  |
| xml_etree_process    | 60.6 ms                                                | 61.7 ms: 1.02x slower                                  |
| xml_etree_parse      | 156 ms                                                 | 159 ms: 1.02x slower                                   |
| xml_etree_generate   | 86.7 ms                                                | 89.2 ms: 1.03x slower                                  |
| pickle_pure_python   | 310 us                                                 | 324 us: 1.04x slower                                   |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                  |
| xml_etree_iterparse  | 101 ms                                                 | 107 ms: 1.05x slower                                   |
| unpickle_pure_python | 216 us                                                 | 230 us: 1.07x slower                                   |
| tomli_loads          | 2.14 sec                                               | 2.33 sec: 1.09x slower                                 |
| Geometric mean       | (ref)                                                  | 1.04x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 9.55 ms: 1.31x faster                                  |
| python_startup_no_site | 6.96 ms                                                | 6.94 ms: 1.00x faster                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 35.2 ms                                                | 34.6 ms: 1.02x faster                                  |
| mako            | 11.1 ms                                                | 11.9 ms: 1.07x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.48 ms: 1.63x faster                                  |
| python_startup             | 12.5 ms                                                | 9.55 ms: 1.31x faster                                  |
| mypy2                      | 1.04 sec                                               | 830 ms: 1.26x faster                                   |
| telco                      | 8.54 ms                                                | 7.10 ms: 1.20x faster                                  |
| coverage                   | 84.0 ms                                                | 72.7 ms: 1.16x faster                                  |
| gc_traversal               | 4.37 ms                                                | 3.79 ms: 1.15x faster                                  |
| regex_v8                   | 26.2 ms                                                | 23.1 ms: 1.13x faster                                  |
| richards_super             | 54.9 ms                                                | 51.5 ms: 1.06x faster                                  |
| richards                   | 48.7 ms                                                | 45.8 ms: 1.06x faster                                  |
| typing_runtime_protocols   | 165 us                                                 | 158 us: 1.04x faster                                   |
| mdp                        | 2.72 sec                                               | 2.63 sec: 1.03x faster                                 |
| regex_effbot               | 3.73 ms                                                | 3.61 ms: 1.03x faster                                  |
| go                         | 144 ms                                                 | 139 ms: 1.03x faster                                   |
| regex_dna                  | 218 ms                                                 | 212 ms: 1.03x faster                                   |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                 |
| json                       | 5.36 ms                                                | 5.26 ms: 1.02x faster                                  |
| json_dumps                 | 10.6 ms                                                | 10.4 ms: 1.02x faster                                  |
| django_template            | 35.2 ms                                                | 34.6 ms: 1.02x faster                                  |
| python_startup_no_site     | 6.96 ms                                                | 6.94 ms: 1.00x faster                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                   |
| xml_etree_process          | 60.6 ms                                                | 61.7 ms: 1.02x slower                                  |
| sqlglot_optimize           | 53.7 ms                                                | 54.8 ms: 1.02x slower                                  |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                  |
| pyflate                    | 471 ms                                                 | 482 ms: 1.02x slower                                   |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                   |
| bench_thread_pool          | 822 us                                                 | 842 us: 1.02x slower                                   |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                   |
| logging_silent             | 102 ns                                                 | 104 ns: 1.03x slower                                   |
| xml_etree_generate         | 86.7 ms                                                | 89.2 ms: 1.03x slower                                  |
| 2to3                       | 267 ms                                                 | 274 ms: 1.03x slower                                   |
| fannkuch                   | 404 ms                                                 | 417 ms: 1.03x slower                                   |
| sympy_expand               | 463 ms                                                 | 478 ms: 1.03x slower                                   |
| meteor_contest             | 109 ms                                                 | 112 ms: 1.03x slower                                   |
| deepcopy                   | 358 us                                                 | 371 us: 1.04x slower                                   |
| hexiom                     | 6.16 ms                                                | 6.41 ms: 1.04x slower                                  |
| deepcopy_memo              | 39.1 us                                                | 40.7 us: 1.04x slower                                  |
| pickle_pure_python         | 310 us                                                 | 324 us: 1.04x slower                                   |
| scimark_sor                | 124 ms                                                 | 129 ms: 1.05x slower                                   |
| deepcopy_reduce            | 3.20 us                                                | 3.35 us: 1.05x slower                                  |
| json_loads                 | 27.2 us                                                | 28.5 us: 1.05x slower                                  |
| scimark_lu                 | 113 ms                                                 | 118 ms: 1.05x slower                                   |
| scimark_fft                | 364 ms                                                 | 382 ms: 1.05x slower                                   |
| pprint_pformat             | 1.49 sec                                               | 1.57 sec: 1.05x slower                                 |
| xml_etree_iterparse        | 101 ms                                                 | 107 ms: 1.05x slower                                   |
| async_generators           | 436 ms                                                 | 463 ms: 1.06x slower                                   |
| nqueens                    | 78.4 ms                                                | 83.3 ms: 1.06x slower                                  |
| sqlglot_transpile          | 1.58 ms                                                | 1.68 ms: 1.06x slower                                  |
| dulwich_log                | 64.3 ms                                                | 68.5 ms: 1.06x slower                                  |
| pprint_safe_repr           | 728 ms                                                 | 776 ms: 1.07x slower                                   |
| unpickle_pure_python       | 216 us                                                 | 230 us: 1.07x slower                                   |
| docutils                   | 2.59 sec                                               | 2.77 sec: 1.07x slower                                 |
| chameleon                  | 6.94 ms                                                | 7.41 ms: 1.07x slower                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.07x slower                                  |
| float                      | 79.2 ms                                                | 84.7 ms: 1.07x slower                                  |
| mako                       | 11.1 ms                                                | 11.9 ms: 1.07x slower                                  |
| sympy_integrate            | 19.9 ms                                                | 21.4 ms: 1.08x slower                                  |
| generators                 | 29.0 ms                                                | 31.2 ms: 1.08x slower                                  |
| crypto_pyaes               | 75.3 ms                                                | 81.9 ms: 1.09x slower                                  |
| tomli_loads                | 2.14 sec                                               | 2.33 sec: 1.09x slower                                 |
| sympy_str                  | 275 ms                                                 | 300 ms: 1.09x slower                                   |
| sqlalchemy_imperative      | 17.1 ms                                                | 18.7 ms: 1.09x slower                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 147 ms: 1.10x slower                                   |
| pathlib                    | 17.5 ms                                                | 19.3 ms: 1.10x slower                                  |
| tornado_http               | 92.4 ms                                                | 103 ms: 1.11x slower                                   |
| scimark_monte_carlo        | 67.4 ms                                                | 75.1 ms: 1.11x slower                                  |
| nbody                      | 87.0 ms                                                | 97.0 ms: 1.12x slower                                  |
| regex_compile              | 132 ms                                                 | 148 ms: 1.12x slower                                   |
| sympy_sum                  | 150 ms                                                 | 169 ms: 1.12x slower                                   |
| logging_simple             | 5.72 us                                                | 6.46 us: 1.13x slower                                  |
| logging_format             | 6.40 us                                                | 7.23 us: 1.13x slower                                  |
| deltablue                  | 3.23 ms                                                | 3.72 ms: 1.15x slower                                  |
| chaos                      | 58.1 ms                                                | 67.0 ms: 1.15x slower                                  |
| raytrace                   | 267 ms                                                 | 312 ms: 1.17x slower                                   |
| async_tree_memoization_tg  | 464 ms                                                 | 575 ms: 1.24x slower                                   |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 726 ms: 1.26x slower                                   |
| async_tree_memoization     | 442 ms                                                 | 578 ms: 1.31x slower                                   |
| comprehensions             | 16.5 us                                                | 21.8 us: 1.32x slower                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 726 ms: 1.33x slower                                   |
| async_tree_none            | 351 ms                                                 | 472 ms: 1.35x slower                                   |
| async_tree_io              | 842 ms                                                 | 1.16 sec: 1.37x slower                                 |
| async_tree_io_tg           | 857 ms                                                 | 1.18 sec: 1.38x slower                                 |
| async_tree_none_tg         | 321 ms                                                 | 450 ms: 1.40x slower                                   |
| Geometric mean             | (ref)                                                  | 1.05x slower                                           |

Benchmark hidden because not significant (4): spectral_norm, asyncio_websockets, bench_mp_pool, scimark_sparse_mat_mult
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, thrift
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.047x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.94x
# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.038x faster
- HPT reliability: 99.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                   |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                 |
| html5lib       | 63.4 ms                                                | 64.8 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                   |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                   |
| async_generators           | 433 ms                                                 | 407 ms: 1.07x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.0 ms: 1.17x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.17 ms: 1.19x faster                                                  |
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                  |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                                   |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                 |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 79.4 ms: 1.09x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 55.3 ms: 1.09x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 196 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 95.0 ms: 1.07x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 309 us: 1.02x slower                                                   |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.0 ms: 1.06x faster                                                  |
| genshi_text     | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                  |
| django_template | 31.7 ms                                                | 33.8 ms: 1.07x slower                                                  |
| genshi_xml      | 50.5 ms                                                | 58.4 ms: 1.16x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                   |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                                   |
| deepcopy                   | 354 us                                                 | 279 us: 1.27x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.4 us: 1.26x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                   |
| spectral_norm              | 113 ms                                                 | 94.4 ms: 1.20x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.17 ms: 1.19x faster                                                  |
| scimark_fft                | 367 ms                                                 | 310 ms: 1.18x faster                                                   |
| float                      | 78.7 ms                                                | 67.0 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.33 ms: 1.16x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                   |
| go                         | 141 ms                                                 | 124 ms: 1.13x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                   |
| richards                   | 47.5 ms                                                | 43.0 ms: 1.11x faster                                                  |
| telco                      | 8.40 ms                                                | 7.62 ms: 1.10x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 79.4 ms: 1.09x faster                                                  |
| richards_super             | 53.7 ms                                                | 49.2 ms: 1.09x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 55.3 ms: 1.09x faster                                                  |
| pathlib                    | 17.4 ms                                                | 15.9 ms: 1.09x faster                                                  |
| pylint                     | 312 ms                                                 | 287 ms: 1.09x faster                                                   |
| unpickle_pure_python       | 213 us                                                 | 196 us: 1.09x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.33 sec: 1.08x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 70.0 ms: 1.07x faster                                                  |
| async_generators           | 433 ms                                                 | 407 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 95.0 ms: 1.07x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 62.7 ms: 1.07x faster                                                  |
| mako                       | 10.7 ms                                                | 10.0 ms: 1.06x faster                                                  |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                   |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                                   |
| thrift                     | 800 us                                                 | 760 us: 1.05x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.72 ms: 1.04x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                 |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| json                       | 5.32 ms                                                | 5.19 ms: 1.03x faster                                                  |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                   |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                   |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                   |
| fannkuch                   | 394 ms                                                 | 390 ms: 1.01x faster                                                   |
| pyflate                    | 470 ms                                                 | 465 ms: 1.01x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| chaos                      | 58.0 ms                                                | 58.6 ms: 1.01x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 309 us: 1.02x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                                 |
| html5lib                   | 63.4 ms                                                | 64.8 ms: 1.02x slower                                                  |
| genshi_text                | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                  |
| logging_format             | 6.23 us                                                | 6.38 us: 1.02x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 744 ms: 1.02x slower                                                   |
| sympy_str                  | 273 ms                                                 | 280 ms: 1.03x slower                                                   |
| logging_simple             | 5.65 us                                                | 5.81 us: 1.03x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 55.0 ms: 1.03x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 66.7 ms: 1.03x slower                                                  |
| sympy_expand               | 456 ms                                                 | 471 ms: 1.03x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 20.5 ms: 1.04x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                  |
| django_template            | 31.7 ms                                                | 33.8 ms: 1.07x slower                                                  |
| logging_silent             | 101 ns                                                 | 109 ns: 1.08x slower                                                   |
| coverage                   | 82.8 ms                                                | 89.6 ms: 1.08x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.47 ms: 1.09x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 891 us: 1.09x slower                                                   |
| raytrace                   | 262 ms                                                 | 288 ms: 1.10x slower                                                   |
| nqueens                    | 80.9 ms                                                | 89.2 ms: 1.10x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                  |
| many_optionals             | 857 us                                                 | 960 us: 1.12x slower                                                   |
| genshi_xml                 | 50.5 ms                                                | 58.4 ms: 1.16x slower                                                  |
| hexiom                     | 6.08 ms                                                | 7.40 ms: 1.22x slower                                                  |
| generators                 | 28.8 ms                                                | 37.4 ms: 1.30x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.8 ms: 3.37x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (5): meteor_contest, asyncio_websockets, nbody, sphinx, mdp
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 99.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
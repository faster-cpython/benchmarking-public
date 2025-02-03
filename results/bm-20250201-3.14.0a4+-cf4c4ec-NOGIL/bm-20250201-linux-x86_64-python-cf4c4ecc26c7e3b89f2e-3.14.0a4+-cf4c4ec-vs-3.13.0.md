# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.082x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 305 ms: 1.15x slower                                                   |
| docutils       | 2.58 sec                                               | 2.80 sec: 1.08x slower                                                 |
| html5lib       | 63.4 ms                                                | 68.3 ms: 1.08x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.12 sec: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 549 ms: 1.57x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 323 ms: 1.43x faster                                                   |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.41x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 243 ms: 1.32x faster                                                   |
| async_tree_none            | 350 ms                                                 | 286 ms: 1.22x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 364 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 523 ms: 1.10x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                   |
| async_generators           | 433 ms                                                 | 435 ms: 1.00x slower                                                   |
| coroutines                 | 22.2 ms                                                | 24.6 ms: 1.11x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 182 ms: 1.03x faster                                                   |
| nbody          | 87.7 ms                                                | 139 ms: 1.59x slower                                                   |
| Geometric mean | (ref)                                                  | 1.16x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.50 ms: 1.08x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                  |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                   |
| regex_compile  | 132 ms                                                 | 147 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 94.6 ms: 1.07x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 95.0 ms: 1.09x slower                                                  |
| xml_etree_process    | 60.5 ms                                                | 67.7 ms: 1.12x slower                                                  |
| tomli_loads          | 2.12 sec                                               | 2.38 sec: 1.12x slower                                                 |
| unpickle_pure_python | 213 us                                                 | 254 us: 1.19x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 368 us: 1.22x slower                                                   |
| json_loads           | 27.2 us                                                | 33.2 us: 1.22x slower                                                  |
| json_dumps           | 10.1 ms                                                | 12.7 ms: 1.26x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.0 ms: 1.19x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 9.36 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 60.5 ms: 1.20x slower                                                  |
| genshi_text     | 22.6 ms                                                | 28.2 ms: 1.25x slower                                                  |
| django_template | 31.7 ms                                                | 40.1 ms: 1.27x slower                                                  |
| mako            | 10.7 ms                                                | 16.3 ms: 1.52x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.30x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 2.25 ms: 2.18x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 549 ms: 1.57x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 323 ms: 1.43x faster                                                   |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.41x faster                                                   |
| create_gc_cycles           | 2.45 ms                                                | 1.75 ms: 1.40x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 243 ms: 1.32x faster                                                   |
| async_tree_none            | 350 ms                                                 | 286 ms: 1.22x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 364 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                   |
| deepcopy                   | 354 us                                                 | 310 us: 1.14x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 523 ms: 1.10x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.50 ms: 1.08x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 94.6 ms: 1.07x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| pidigits                   | 186 ms                                                 | 182 ms: 1.03x faster                                                   |
| go                         | 141 ms                                                 | 141 ms: 1.00x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                   |
| async_generators           | 433 ms                                                 | 435 ms: 1.00x slower                                                   |
| spectral_norm              | 113 ms                                                 | 115 ms: 1.02x slower                                                   |
| deepcopy_memo              | 38.4 us                                                | 39.1 us: 1.02x slower                                                  |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                                   |
| k_core                     | 2.37 sec                                               | 2.45 sec: 1.03x slower                                                 |
| generators                 | 28.8 ms                                                | 30.2 ms: 1.05x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.97 sec: 1.06x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 68.9 ms: 1.07x slower                                                  |
| json                       | 5.32 ms                                                | 5.70 ms: 1.07x slower                                                  |
| html5lib                   | 63.4 ms                                                | 68.3 ms: 1.08x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.80 sec: 1.08x slower                                                 |
| sphinx                     | 1.03 sec                                               | 1.12 sec: 1.09x slower                                                 |
| pyflate                    | 470 ms                                                 | 510 ms: 1.09x slower                                                   |
| telco                      | 8.40 ms                                                | 9.18 ms: 1.09x slower                                                  |
| xml_etree_generate         | 86.8 ms                                                | 95.0 ms: 1.09x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 118 ms: 1.10x slower                                                   |
| logging_silent             | 101 ns                                                 | 111 ns: 1.10x slower                                                   |
| coroutines                 | 22.2 ms                                                | 24.6 ms: 1.11x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.84 sec: 1.12x slower                                                 |
| regex_compile              | 132 ms                                                 | 147 ms: 1.12x slower                                                   |
| xml_etree_process          | 60.5 ms                                                | 67.7 ms: 1.12x slower                                                  |
| tomli_loads                | 2.12 sec                                               | 2.38 sec: 1.12x slower                                                 |
| sqlglot_optimize           | 53.4 ms                                                | 60.1 ms: 1.13x slower                                                  |
| scimark_sor                | 122 ms                                                 | 138 ms: 1.13x slower                                                   |
| scimark_fft                | 367 ms                                                 | 419 ms: 1.14x slower                                                   |
| sympy_expand               | 456 ms                                                 | 521 ms: 1.14x slower                                                   |
| richards                   | 47.5 ms                                                | 54.4 ms: 1.14x slower                                                  |
| 2to3                       | 266 ms                                                 | 305 ms: 1.15x slower                                                   |
| sympy_str                  | 273 ms                                                 | 315 ms: 1.15x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.16x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 841 ms: 1.16x slower                                                   |
| logging_simple             | 5.65 us                                                | 6.60 us: 1.17x slower                                                  |
| thrift                     | 800 us                                                 | 935 us: 1.17x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.73 sec: 1.17x slower                                                 |
| shortest_path              | 487 ms                                                 | 572 ms: 1.18x slower                                                   |
| richards_super             | 53.7 ms                                                | 63.3 ms: 1.18x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 23.4 ms: 1.18x slower                                                  |
| logging_format             | 6.23 us                                                | 7.38 us: 1.18x slower                                                  |
| connected_components       | 447 ms                                                 | 530 ms: 1.19x slower                                                   |
| python_startup             | 12.7 ms                                                | 15.0 ms: 1.19x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 88.7 ms: 1.19x slower                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 159 ms: 1.19x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 254 us: 1.19x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.3 ms: 1.20x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 60.5 ms: 1.20x slower                                                  |
| meteor_contest             | 108 ms                                                 | 131 ms: 1.21x slower                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.09 ms: 1.21x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.90 ms: 1.21x slower                                                  |
| comprehensions             | 16.5 us                                                | 20.0 us: 1.21x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 368 us: 1.22x slower                                                   |
| json_loads                 | 27.2 us                                                | 33.2 us: 1.22x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 140 ms: 1.23x slower                                                   |
| nqueens                    | 80.9 ms                                                | 99.6 ms: 1.23x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.57 ms: 1.24x slower                                                  |
| genshi_text                | 22.6 ms                                                | 28.2 ms: 1.25x slower                                                  |
| many_optionals             | 857 us                                                 | 1.07 ms: 1.25x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 12.7 ms: 1.26x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 202 us: 1.26x slower                                                   |
| django_template            | 31.7 ms                                                | 40.1 ms: 1.27x slower                                                  |
| chaos                      | 58.0 ms                                                | 74.6 ms: 1.29x slower                                                  |
| hexiom                     | 6.08 ms                                                | 7.85 ms: 1.29x slower                                                  |
| coverage                   | 82.8 ms                                                | 107 ms: 1.29x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 87.6 ms: 1.31x slower                                                  |
| fannkuch                   | 394 ms                                                 | 519 ms: 1.32x slower                                                   |
| raytrace                   | 262 ms                                                 | 349 ms: 1.34x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 9.36 ms: 1.34x slower                                                  |
| deltablue                  | 3.19 ms                                                | 4.73 ms: 1.48x slower                                                  |
| mako                       | 10.7 ms                                                | 16.3 ms: 1.52x slower                                                  |
| subparsers                 | 15.5 ms                                                | 24.3 ms: 1.57x slower                                                  |
| nbody                      | 87.7 ms                                                | 139 ms: 1.59x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 84.8 ms: 3.54x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 3.48 ms: 4.26x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.12x slower                                                           |

Benchmark hidden because not significant (4): pylint, float, deepcopy_reduce, pycparser
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.082x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.22x
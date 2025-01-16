# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_refcounts
- machine: linux-x86_64
- commit hash: 5501f0a
- commit date: 2025-01-15
- overall geometric mean: 1.030x faster
- HPT reliability: 98.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                       |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                     |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 593 ms: 1.45x faster                                                       |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.36x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 332 ms: 1.32x faster                                                       |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 503 ms: 1.14x faster                                                       |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                       |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.4 ms: 1.12x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| nbody          | 87.7 ms                                                | 91.8 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.05 ms: 1.24x faster                                                      |
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                      |
| regex_dna      | 220 ms                                                 | 203 ms: 1.08x faster                                                       |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                     |
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 79.1 ms: 1.10x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 55.3 ms: 1.09x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 197 us: 1.08x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 95.0 ms: 1.07x faster                                                      |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                       |
| json_loads           | 27.2 us                                                | 29.6 us: 1.09x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                      |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.91 ms: 1.08x faster                                                      |
| genshi_text     | 22.6 ms                                                | 24.0 ms: 1.06x slower                                                      |
| django_template | 31.7 ms                                                | 33.7 ms: 1.06x slower                                                      |
| genshi_xml      | 50.5 ms                                                | 59.2 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250115-linux-x86_64-brandtbucher-tier_two_refcounts-3.14.0a4+-5501f0a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 593 ms: 1.45x faster                                                       |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.36x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 332 ms: 1.32x faster                                                       |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                       |
| deepcopy                   | 354 us                                                 | 272 us: 1.30x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 30.2 us: 1.27x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.05 ms: 1.24x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.19x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                     |
| scimark_fft                | 367 ms                                                 | 319 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 503 ms: 1.14x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                       |
| float                      | 78.7 ms                                                | 70.4 ms: 1.12x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.58 ms: 1.10x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 79.1 ms: 1.10x faster                                                      |
| telco                      | 8.40 ms                                                | 7.67 ms: 1.10x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 55.3 ms: 1.09x faster                                                      |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                       |
| pylint                     | 312 ms                                                 | 287 ms: 1.09x faster                                                       |
| unpickle_pure_python       | 213 us                                                 | 197 us: 1.08x faster                                                       |
| crypto_pyaes               | 74.7 ms                                                | 68.9 ms: 1.08x faster                                                      |
| richards                   | 47.5 ms                                                | 44.0 ms: 1.08x faster                                                      |
| regex_dna                  | 220 ms                                                 | 203 ms: 1.08x faster                                                       |
| mako                       | 10.7 ms                                                | 9.91 ms: 1.08x faster                                                      |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.07x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                     |
| scimark_monte_carlo        | 66.8 ms                                                | 62.6 ms: 1.07x faster                                                      |
| richards_super             | 53.7 ms                                                | 50.4 ms: 1.07x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 95.0 ms: 1.07x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                      |
| pyflate                    | 470 ms                                                 | 445 ms: 1.06x faster                                                       |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.06x faster                                                      |
| go                         | 141 ms                                                 | 135 ms: 1.04x faster                                                       |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                     |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                       |
| thrift                     | 800 us                                                 | 773 us: 1.03x faster                                                       |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                       |
| fannkuch                   | 394 ms                                                 | 386 ms: 1.02x faster                                                       |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                       |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                                       |
| json                       | 5.32 ms                                                | 5.25 ms: 1.01x faster                                                      |
| shortest_path              | 487 ms                                                 | 481 ms: 1.01x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                       |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                       |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.00x faster                                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.00x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                      |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                      |
| mdp                        | 2.54 sec                                               | 2.57 sec: 1.01x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                       |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                      |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.01x slower                                                     |
| deltablue                  | 3.19 ms                                                | 3.25 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 727 ms                                                 | 741 ms: 1.02x slower                                                       |
| logging_format             | 6.23 us                                                | 6.38 us: 1.02x slower                                                      |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                                      |
| logging_simple             | 5.65 us                                                | 5.83 us: 1.03x slower                                                      |
| sympy_str                  | 273 ms                                                 | 282 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 53.4 ms                                                | 55.3 ms: 1.04x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                                       |
| dulwich_log                | 64.6 ms                                                | 67.1 ms: 1.04x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                     |
| sympy_expand               | 456 ms                                                 | 476 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.05x slower                                                       |
| nbody                      | 87.7 ms                                                | 91.8 ms: 1.05x slower                                                      |
| sympy_integrate            | 19.8 ms                                                | 20.8 ms: 1.05x slower                                                      |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                      |
| chaos                      | 58.0 ms                                                | 61.1 ms: 1.05x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.5 us: 1.06x slower                                                      |
| genshi_text                | 22.6 ms                                                | 24.0 ms: 1.06x slower                                                      |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                       |
| django_template            | 31.7 ms                                                | 33.7 ms: 1.06x slower                                                      |
| json_loads                 | 27.2 us                                                | 29.6 us: 1.09x slower                                                      |
| coverage                   | 82.8 ms                                                | 90.3 ms: 1.09x slower                                                      |
| raytrace                   | 262 ms                                                 | 286 ms: 1.10x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 898 us: 1.10x slower                                                       |
| nqueens                    | 80.9 ms                                                | 90.3 ms: 1.12x slower                                                      |
| many_optionals             | 857 us                                                 | 979 us: 1.14x slower                                                       |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                      |
| genshi_xml                 | 50.5 ms                                                | 59.2 ms: 1.17x slower                                                      |
| hexiom                     | 6.08 ms                                                | 7.13 ms: 1.17x slower                                                      |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                      |
| generators                 | 28.8 ms                                                | 40.2 ms: 1.40x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (5): pycparser, html5lib, sqlalchemy_imperative, asyncio_websockets, pprint_pformat
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 98.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
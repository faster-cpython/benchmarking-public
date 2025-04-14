# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_generators
- machine: linux-x86_64
- commit hash: 346d1bc
- commit date: 2025-02-04
- overall geometric mean: 1.042x faster
- HPT reliability: 99.10%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                  |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| html5lib       | 63.4 ms                                                | 62.5 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                  |
| async_tree_io              | 838 ms                                                 | 622 ms: 1.35x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 327 ms: 1.34x faster                                                  |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                  |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                                  |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.04x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.4 ms: 1.17x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| nbody          | 87.7 ms                                                | 90.1 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.97 ms: 1.27x faster                                                 |
| regex_dna      | 220 ms                                                 | 194 ms: 1.13x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                 |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.17x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 79.7 ms: 1.09x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 56.1 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 94.6 ms: 1.07x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                                  |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                 |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                 |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                 |
| genshi_text     | 22.6 ms                                                | 23.0 ms: 1.02x slower                                                 |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                 |
| genshi_xml      | 50.5 ms                                                | 54.4 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                  |
| async_tree_io              | 838 ms                                                 | 622 ms: 1.35x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 327 ms: 1.34x faster                                                  |
| deepcopy                   | 354 us                                                 | 269 us: 1.32x faster                                                  |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 2.97 ms: 1.27x faster                                                 |
| deepcopy_memo              | 38.4 us                                                | 30.6 us: 1.25x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                  |
| spectral_norm              | 113 ms                                                 | 93.4 ms: 1.21x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                                 |
| scimark_fft                | 367 ms                                                 | 311 ms: 1.18x faster                                                  |
| float                      | 78.7 ms                                                | 67.4 ms: 1.17x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.17x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                  |
| regex_dna                  | 220 ms                                                 | 194 ms: 1.13x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                  |
| go                         | 141 ms                                                 | 127 ms: 1.11x faster                                                  |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                  |
| telco                      | 8.40 ms                                                | 7.62 ms: 1.10x faster                                                 |
| richards                   | 47.5 ms                                                | 43.3 ms: 1.10x faster                                                 |
| pathlib                    | 17.4 ms                                                | 15.9 ms: 1.09x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 79.7 ms: 1.09x faster                                                 |
| richards_super             | 53.7 ms                                                | 49.5 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.64 ms: 1.08x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 56.1 ms: 1.08x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 94.6 ms: 1.07x faster                                                 |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.07x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 62.6 ms: 1.07x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 70.1 ms: 1.07x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 201 us: 1.06x faster                                                  |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                                  |
| mako                       | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                 |
| thrift                     | 800 us                                                 | 767 us: 1.04x faster                                                  |
| json                       | 5.32 ms                                                | 5.13 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                  |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                  |
| pyflate                    | 470 ms                                                 | 460 ms: 1.02x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                  |
| html5lib                   | 63.4 ms                                                | 62.5 ms: 1.01x faster                                                 |
| logging_format             | 6.23 us                                                | 6.16 us: 1.01x faster                                                 |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| connected_components       | 447 ms                                                 | 443 ms: 1.01x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                 |
| gc_traversal               | 4.90 ms                                                | 4.86 ms: 1.01x faster                                                 |
| shortest_path              | 487 ms                                                 | 483 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.45 ms: 1.00x slower                                                 |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.56 sec: 1.01x slower                                                |
| python_startup_no_site     | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                 |
| sqlglot_optimize           | 53.4 ms                                                | 53.9 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.02x slower                                                |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                 |
| genshi_text                | 22.6 ms                                                | 23.0 ms: 1.02x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 741 ms: 1.02x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                  |
| sympy_str                  | 273 ms                                                 | 279 ms: 1.02x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                                  |
| nbody                      | 87.7 ms                                                | 90.1 ms: 1.03x slower                                                 |
| sympy_expand               | 456 ms                                                 | 470 ms: 1.03x slower                                                  |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                 |
| chaos                      | 58.0 ms                                                | 60.0 ms: 1.03x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 66.8 ms: 1.03x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| sympy_integrate            | 19.8 ms                                                | 20.5 ms: 1.04x slower                                                 |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.04x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                 |
| genshi_xml                 | 50.5 ms                                                | 54.4 ms: 1.08x slower                                                 |
| logging_silent             | 101 ns                                                 | 109 ns: 1.08x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 892 us: 1.09x slower                                                  |
| coverage                   | 82.8 ms                                                | 90.7 ms: 1.09x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.51 ms: 1.10x slower                                                 |
| raytrace                   | 262 ms                                                 | 289 ms: 1.10x slower                                                  |
| nqueens                    | 80.9 ms                                                | 89.8 ms: 1.11x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.11x slower                                                 |
| many_optionals             | 857 us                                                 | 962 us: 1.12x slower                                                  |
| hexiom                     | 6.08 ms                                                | 7.42 ms: 1.22x slower                                                 |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.34x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 81.0 ms: 3.38x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (6): sphinx, logging_simple, fannkuch, generators, asyncio_websockets, pycparser
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x
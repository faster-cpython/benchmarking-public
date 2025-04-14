# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_validity
- machine: linux-x86_64
- commit hash: aee117b
- commit date: 2025-02-18
- overall geometric mean: 1.052x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.03x faster                                                |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.02x slower                                              |
| html5lib       | 63.4 ms                                                | 61.4 ms: 1.03x faster                                               |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                               |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.8 ms: 1.13x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| nbody          | 87.7 ms                                                | 91.6 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.16x faster                                               |
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                               |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.80 sec: 1.18x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.12x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 77.6 ms: 1.12x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 55.4 ms: 1.09x faster                                               |
| unpickle_pure_python | 213 us                                                 | 200 us: 1.06x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 96.4 ms: 1.05x faster                                               |
| json_loads           | 27.2 us                                                | 28.7 us: 1.06x slower                                               |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.08x slower                                                |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.18x slower                                               |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.04 ms: 1.01x slower                                               |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.06x faster                                               |
| mako            | 10.7 ms                                                | 10.2 ms: 1.05x faster                                               |
| genshi_xml      | 50.5 ms                                                | 48.8 ms: 1.03x faster                                               |
| django_template | 31.7 ms                                                | 31.8 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 30.5 us: 1.26x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                               |
| scimark_fft                | 367 ms                                                 | 305 ms: 1.20x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.80 sec: 1.18x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.32 ms: 1.16x faster                                               |
| spectral_norm              | 113 ms                                                 | 97.4 ms: 1.16x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                |
| go                         | 141 ms                                                 | 124 ms: 1.14x faster                                                |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                               |
| float                      | 78.7 ms                                                | 69.8 ms: 1.13x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.12x faster                                                |
| pylint                     | 312 ms                                                 | 277 ms: 1.12x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 77.6 ms: 1.12x faster                                               |
| telco                      | 8.40 ms                                                | 7.54 ms: 1.11x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.10 sec: 1.09x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 55.4 ms: 1.09x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.34 sec: 1.08x faster                                              |
| richards                   | 47.5 ms                                                | 44.1 ms: 1.08x faster                                               |
| pathlib                    | 17.4 ms                                                | 16.1 ms: 1.08x faster                                               |
| richards_super             | 53.7 ms                                                | 50.4 ms: 1.07x faster                                               |
| thrift                     | 800 us                                                 | 751 us: 1.07x faster                                                |
| unpickle_pure_python       | 213 us                                                 | 200 us: 1.06x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.06x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                               |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                |
| crypto_pyaes               | 74.7 ms                                                | 70.8 ms: 1.05x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 96.4 ms: 1.05x faster                                               |
| mako                       | 10.7 ms                                                | 10.2 ms: 1.05x faster                                               |
| async_generators           | 433 ms                                                 | 415 ms: 1.04x faster                                                |
| json                       | 5.32 ms                                                | 5.11 ms: 1.04x faster                                               |
| logging_simple             | 5.65 us                                                | 5.45 us: 1.04x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 48.8 ms: 1.03x faster                                               |
| connected_components       | 447 ms                                                 | 432 ms: 1.03x faster                                                |
| 2to3                       | 266 ms                                                 | 257 ms: 1.03x faster                                                |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.03x faster                                                |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                                |
| html5lib                   | 63.4 ms                                                | 61.4 ms: 1.03x faster                                               |
| shortest_path              | 487 ms                                                 | 472 ms: 1.03x faster                                                |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                               |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                              |
| pprint_safe_repr           | 727 ms                                                 | 705 ms: 1.03x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                |
| pprint_pformat             | 1.48 sec                                               | 1.44 sec: 1.03x faster                                              |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                |
| logging_format             | 6.23 us                                                | 6.08 us: 1.02x faster                                               |
| pyflate                    | 470 ms                                                 | 460 ms: 1.02x faster                                                |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                                |
| mdp                        | 2.54 sec                                               | 2.51 sec: 1.01x faster                                              |
| typing_runtime_protocols   | 160 us                                                 | 158 us: 1.01x faster                                                |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                               |
| sqlglot_optimize           | 53.4 ms                                                | 52.9 ms: 1.01x faster                                               |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.88 ms: 1.00x faster                                               |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.01x slower                                               |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.01x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 7.04 ms: 1.01x slower                                               |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                               |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                               |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                               |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                               |
| nqueens                    | 80.9 ms                                                | 82.4 ms: 1.02x slower                                               |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                                |
| dulwich_log                | 64.6 ms                                                | 66.1 ms: 1.02x slower                                               |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.02x slower                                              |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                                |
| chaos                      | 58.0 ms                                                | 59.5 ms: 1.02x slower                                               |
| deltablue                  | 3.19 ms                                                | 3.32 ms: 1.04x slower                                               |
| nbody                      | 87.7 ms                                                | 91.6 ms: 1.04x slower                                               |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                               |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.06x slower                                               |
| bench_thread_pool          | 818 us                                                 | 872 us: 1.07x slower                                                |
| hexiom                     | 6.08 ms                                                | 6.53 ms: 1.07x slower                                               |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.08x slower                                                |
| coverage                   | 82.8 ms                                                | 90.3 ms: 1.09x slower                                               |
| many_optionals             | 857 us                                                 | 955 us: 1.11x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.18x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                               |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (5): sympy_str, scimark_monte_carlo, fannkuch, asyncio_websockets, scimark_lu
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x
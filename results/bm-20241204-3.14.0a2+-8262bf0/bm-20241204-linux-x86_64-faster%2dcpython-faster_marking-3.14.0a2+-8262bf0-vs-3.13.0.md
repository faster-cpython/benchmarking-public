# Results vs. 3.13.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 8262bf0
- commit date: 2024-12-04
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 255 ms: 1.05x faster                                                       |
| docutils       | 2.59 sec                                               | 2.58 sec: 1.01x faster                                                     |
| html5lib       | 64.2 ms                                                | 63.2 ms: 1.02x faster                                                      |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 336 ms: 1.38x faster                                                       |
| async_tree_io              | 842 ms                                                 | 610 ms: 1.38x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 621 ms: 1.38x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 340 ms: 1.30x faster                                                       |
| async_tree_none            | 351 ms                                                 | 273 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 268 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 502 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 498 ms: 1.10x faster                                                       |
| async_generators           | 436 ms                                                 | 423 ms: 1.03x faster                                                       |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                       |
| coroutines                 | 22.7 ms                                                | 23.7 ms: 1.05x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.8 ms: 1.02x faster                                                      |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| nbody          | 87.0 ms                                                | 96.3 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.39 ms: 1.10x faster                                                      |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| regex_v8       | 26.2 ms                                                | 25.9 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.08x faster                                                       |
| json_loads           | 27.2 us                                                | 26.3 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 98.1 ms: 1.03x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                     |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                       |
| xml_etree_generate   | 86.7 ms                                                | 87.5 ms: 1.01x slower                                                      |
| pickle_pure_python   | 310 us                                                 | 325 us: 1.05x slower                                                       |
| json_dumps           | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                      |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 32.6 ms: 1.08x faster                                                      |
| genshi_text     | 23.5 ms                                                | 22.9 ms: 1.03x faster                                                      |
| genshi_xml      | 50.9 ms                                                | 49.8 ms: 1.02x faster                                                      |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 336 ms: 1.38x faster                                                       |
| async_tree_io              | 842 ms                                                 | 610 ms: 1.38x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 621 ms: 1.38x faster                                                       |
| deepcopy                   | 358 us                                                 | 261 us: 1.37x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 340 ms: 1.30x faster                                                       |
| async_tree_none            | 351 ms                                                 | 273 ms: 1.28x faster                                                       |
| deepcopy_memo              | 39.1 us                                                | 30.6 us: 1.28x faster                                                      |
| go                         | 144 ms                                                 | 117 ms: 1.22x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 268 ms: 1.20x faster                                                       |
| pylint                     | 313 ms                                                 | 265 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.73 us: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 502 ms: 1.15x faster                                                       |
| json                       | 5.36 ms                                                | 4.85 ms: 1.10x faster                                                      |
| regex_effbot               | 3.73 ms                                                | 3.39 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 498 ms: 1.10x faster                                                       |
| mdp                        | 2.72 sec                                               | 2.51 sec: 1.09x faster                                                     |
| telco                      | 8.54 ms                                                | 7.88 ms: 1.08x faster                                                      |
| django_template            | 35.2 ms                                                | 32.6 ms: 1.08x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.23 ms: 1.08x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.08x faster                                                       |
| k_core                     | 2.35 sec                                               | 2.21 sec: 1.06x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.5 ms: 1.06x faster                                                      |
| thrift                     | 809 us                                                 | 765 us: 1.06x faster                                                       |
| bpe_tokeniser              | 4.75 sec                                               | 4.51 sec: 1.05x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                       |
| logging_format             | 6.40 us                                                | 6.10 us: 1.05x faster                                                      |
| 2to3                       | 267 ms                                                 | 255 ms: 1.05x faster                                                       |
| crypto_pyaes               | 75.3 ms                                                | 72.0 ms: 1.05x faster                                                      |
| richards                   | 48.7 ms                                                | 46.6 ms: 1.04x faster                                                      |
| richards_super             | 54.9 ms                                                | 52.9 ms: 1.04x faster                                                      |
| json_loads                 | 27.2 us                                                | 26.3 us: 1.03x faster                                                      |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.5 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 98.1 ms: 1.03x faster                                                      |
| async_generators           | 436 ms                                                 | 423 ms: 1.03x faster                                                       |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                     |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                       |
| logging_simple             | 5.72 us                                                | 5.56 us: 1.03x faster                                                      |
| genshi_text                | 23.5 ms                                                | 22.9 ms: 1.03x faster                                                      |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                       |
| sympy_str                  | 275 ms                                                 | 269 ms: 1.02x faster                                                       |
| genshi_xml                 | 50.9 ms                                                | 49.8 ms: 1.02x faster                                                      |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                     |
| float                      | 79.2 ms                                                | 77.8 ms: 1.02x faster                                                      |
| generators                 | 29.0 ms                                                | 28.5 ms: 1.02x faster                                                      |
| html5lib                   | 64.2 ms                                                | 63.2 ms: 1.02x faster                                                      |
| sympy_expand               | 463 ms                                                 | 457 ms: 1.01x faster                                                       |
| regex_v8                   | 26.2 ms                                                | 25.9 ms: 1.01x faster                                                      |
| pyflate                    | 471 ms                                                 | 466 ms: 1.01x faster                                                       |
| connected_components       | 444 ms                                                 | 439 ms: 1.01x faster                                                       |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                       |
| docutils                   | 2.59 sec                                               | 2.58 sec: 1.01x faster                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 53.4 ms: 1.01x faster                                                      |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                      |
| deltablue                  | 3.23 ms                                                | 3.22 ms: 1.00x faster                                                      |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                       |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                       |
| dulwich_log                | 64.3 ms                                                | 64.7 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 728 ms                                                 | 735 ms: 1.01x slower                                                       |
| xml_etree_generate         | 86.7 ms                                                | 87.5 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                      |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.61 ms: 1.02x slower                                                      |
| raytrace                   | 267 ms                                                 | 272 ms: 1.02x slower                                                       |
| gc_traversal               | 4.37 ms                                                | 4.45 ms: 1.02x slower                                                      |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                                       |
| hexiom                     | 6.16 ms                                                | 6.28 ms: 1.02x slower                                                      |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                      |
| scimark_fft                | 364 ms                                                 | 372 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 69.0 ms: 1.02x slower                                                      |
| nqueens                    | 78.4 ms                                                | 80.2 ms: 1.02x slower                                                      |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.17 ms: 1.02x slower                                                      |
| bench_thread_pool          | 822 us                                                 | 849 us: 1.03x slower                                                       |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.04x slower                                                       |
| chaos                      | 58.1 ms                                                | 60.5 ms: 1.04x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.7 ms: 1.05x slower                                                      |
| pickle_pure_python         | 310 us                                                 | 325 us: 1.05x slower                                                       |
| logging_silent             | 102 ns                                                 | 107 ns: 1.05x slower                                                       |
| json_dumps                 | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                      |
| nbody                      | 87.0 ms                                                | 96.3 ms: 1.11x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 78.4 ms: 3.27x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (8): fannkuch, typing_runtime_protocols, shortest_path, pprint_pformat, sqlglot_normalize, coverage, regex_dna, xml_etree_process
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241204-3.14.0a2+-8262bf0/bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x
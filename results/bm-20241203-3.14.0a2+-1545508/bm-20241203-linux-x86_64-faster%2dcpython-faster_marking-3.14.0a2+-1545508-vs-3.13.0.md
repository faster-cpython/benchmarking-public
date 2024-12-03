# Results vs. 3.13.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 1545508
- commit date: 2024-12-03
- overall geometric mean: 1.036x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 842 ms                                                 | 632 ms: 1.33x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 349 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 673 ms: 1.27x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 348 ms: 1.27x faster                                                       |
| async_tree_none            | 351 ms                                                 | 284 ms: 1.24x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 283 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 510 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 502 ms: 1.09x faster                                                       |
| async_generators           | 436 ms                                                 | 429 ms: 1.02x faster                                                       |
| coroutines                 | 22.7 ms                                                | 24.1 ms: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.15x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| nbody          | 87.0 ms                                                | 93.7 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.36 ms: 1.11x faster                                                      |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| regex_v8       | 26.2 ms                                                | 26.1 ms: 1.00x faster                                                      |
| regex_dna      | 218 ms                                                 | 225 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                       |
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                     |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                       |
| xml_etree_generate   | 86.7 ms                                                | 87.7 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                                       |
| pickle_pure_python   | 310 us                                                 | 334 us: 1.08x slower                                                       |
| json_dumps           | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                      |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 31.9 ms: 1.10x faster                                                      |
| genshi_text     | 23.5 ms                                                | 22.7 ms: 1.04x faster                                                      |
| genshi_xml      | 50.9 ms                                                | 50.2 ms: 1.01x faster                                                      |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 260 us: 1.38x faster                                                       |
| async_tree_io              | 842 ms                                                 | 632 ms: 1.33x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 349 ms: 1.33x faster                                                       |
| deepcopy_memo              | 39.1 us                                                | 30.4 us: 1.29x faster                                                      |
| async_tree_io_tg           | 857 ms                                                 | 673 ms: 1.27x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 348 ms: 1.27x faster                                                       |
| async_tree_none            | 351 ms                                                 | 284 ms: 1.24x faster                                                       |
| go                         | 144 ms                                                 | 120 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                                      |
| pylint                     | 313 ms                                                 | 273 ms: 1.15x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 283 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 510 ms: 1.13x faster                                                       |
| json                       | 5.36 ms                                                | 4.79 ms: 1.12x faster                                                      |
| regex_effbot               | 3.73 ms                                                | 3.36 ms: 1.11x faster                                                      |
| django_template            | 35.2 ms                                                | 31.9 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 502 ms: 1.09x faster                                                       |
| telco                      | 8.54 ms                                                | 7.86 ms: 1.09x faster                                                      |
| mdp                        | 2.72 sec                                               | 2.50 sec: 1.09x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.3 ms: 1.08x faster                                                      |
| create_gc_cycles           | 2.41 ms                                                | 2.24 ms: 1.07x faster                                                      |
| thrift                     | 809 us                                                 | 764 us: 1.06x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                       |
| richards                   | 48.7 ms                                                | 46.4 ms: 1.05x faster                                                      |
| logging_format             | 6.40 us                                                | 6.12 us: 1.05x faster                                                      |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.84 ms: 1.04x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                       |
| richards_super             | 54.9 ms                                                | 52.8 ms: 1.04x faster                                                      |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.57 sec: 1.04x faster                                                     |
| pyflate                    | 471 ms                                                 | 454 ms: 1.04x faster                                                       |
| genshi_text                | 23.5 ms                                                | 22.7 ms: 1.04x faster                                                      |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                     |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                      |
| crypto_pyaes               | 75.3 ms                                                | 73.5 ms: 1.02x faster                                                      |
| logging_simple             | 5.72 us                                                | 5.59 us: 1.02x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                       |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                       |
| async_generators           | 436 ms                                                 | 429 ms: 1.02x faster                                                       |
| generators                 | 29.0 ms                                                | 28.5 ms: 1.02x faster                                                      |
| genshi_xml                 | 50.9 ms                                                | 50.2 ms: 1.01x faster                                                      |
| sympy_str                  | 275 ms                                                 | 271 ms: 1.01x faster                                                       |
| sympy_expand               | 463 ms                                                 | 459 ms: 1.01x faster                                                       |
| connected_components       | 444 ms                                                 | 440 ms: 1.01x faster                                                       |
| typing_runtime_protocols   | 165 us                                                 | 164 us: 1.01x faster                                                       |
| coverage                   | 84.0 ms                                                | 83.5 ms: 1.01x faster                                                      |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x faster                                                       |
| regex_v8                   | 26.2 ms                                                | 26.1 ms: 1.00x faster                                                      |
| dulwich_log                | 64.3 ms                                                | 64.6 ms: 1.00x slower                                                      |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| sqlglot_normalize          | 108 ms                                                 | 108 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                       |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                      |
| hexiom                     | 6.16 ms                                                | 6.23 ms: 1.01x slower                                                      |
| xml_etree_generate         | 86.7 ms                                                | 87.7 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 728 ms                                                 | 737 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.61 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 68.6 ms: 1.02x slower                                                      |
| raytrace                   | 267 ms                                                 | 272 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                                       |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                      |
| gc_traversal               | 4.37 ms                                                | 4.47 ms: 1.02x slower                                                      |
| deltablue                  | 3.23 ms                                                | 3.30 ms: 1.02x slower                                                      |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                      |
| k_core                     | 2.35 sec                                               | 2.42 sec: 1.03x slower                                                     |
| regex_dna                  | 218 ms                                                 | 225 ms: 1.03x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                      |
| bench_thread_pool          | 822 us                                                 | 853 us: 1.04x slower                                                       |
| scimark_sor                | 124 ms                                                 | 128 ms: 1.04x slower                                                       |
| chaos                      | 58.1 ms                                                | 60.5 ms: 1.04x slower                                                      |
| nqueens                    | 78.4 ms                                                | 82.9 ms: 1.06x slower                                                      |
| coroutines                 | 22.7 ms                                                | 24.1 ms: 1.06x slower                                                      |
| logging_silent             | 102 ns                                                 | 108 ns: 1.06x slower                                                       |
| pickle_pure_python         | 310 us                                                 | 334 us: 1.08x slower                                                       |
| nbody                      | 87.0 ms                                                | 93.7 ms: 1.08x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.8 ms: 3.37x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (12): sphinx, shortest_path, docutils, sqlglot_optimize, float, html5lib, sympy_integrate, pprint_pformat, asyncio_websockets, xml_etree_process, fannkuch, scimark_fft
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241203-3.14.0a2+-1545508/bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
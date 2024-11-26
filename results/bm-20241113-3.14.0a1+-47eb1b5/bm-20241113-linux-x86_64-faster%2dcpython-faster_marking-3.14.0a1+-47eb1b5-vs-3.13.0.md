# Results vs. 3.13.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 47eb1b5
- commit date: 2024-11-13
- overall geometric mean: 1.049x faster
- HPT reliability: 99.20%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 260 ms: 1.03x faster                                                       |
| docutils       | 2.59 sec                                               | 2.61 sec: 1.01x slower                                                     |
| html5lib       | 64.2 ms                                                | 65.4 ms: 1.02x slower                                                      |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 842 ms                                                 | 596 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 619 ms: 1.38x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 337 ms: 1.38x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 345 ms: 1.28x faster                                                       |
| async_tree_none            | 351 ms                                                 | 278 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 276 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 504 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 493 ms: 1.11x faster                                                       |
| async_generators           | 436 ms                                                 | 431 ms: 1.01x faster                                                       |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                       |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| float          | 79.2 ms                                                | 83.9 ms: 1.06x slower                                                      |
| nbody          | 87.0 ms                                                | 98.4 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.9 ms: 1.05x faster                                                      |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| regex_effbot   | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                      |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.04 sec: 1.05x faster                                                     |
| json_loads           | 27.2 us                                                | 26.1 us: 1.04x faster                                                      |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.00x slower                                                       |
| xml_etree_generate   | 86.7 ms                                                | 87.2 ms: 1.01x slower                                                      |
| xml_etree_process    | 60.6 ms                                                | 61.2 ms: 1.01x slower                                                      |
| pickle_pure_python   | 310 us                                                 | 328 us: 1.06x slower                                                       |
| json_dumps           | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                      |
| xml_etree_parse      | 156 ms                                                 | 172 ms: 1.11x slower                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 120 ms: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 6.79 ms: 1.03x faster                                                      |
| python_startup         | 12.5 ms                                                | 12.4 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.1 ms: 1.06x faster                                                      |
| django_template | 35.2 ms                                                | 34.5 ms: 1.02x faster                                                      |
| genshi_xml      | 50.9 ms                                                | 51.6 ms: 1.01x slower                                                      |
| mako            | 11.1 ms                                                | 11.7 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 4.37 ms                                                | 1.74 ms: 2.51x faster                                                      |
| create_gc_cycles           | 2.41 ms                                                | 1.64 ms: 1.47x faster                                                      |
| async_tree_io              | 842 ms                                                 | 596 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 619 ms: 1.38x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 337 ms: 1.38x faster                                                       |
| deepcopy                   | 358 us                                                 | 264 us: 1.35x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 345 ms: 1.28x faster                                                       |
| deepcopy_memo              | 39.1 us                                                | 30.5 us: 1.28x faster                                                      |
| async_tree_none            | 351 ms                                                 | 278 ms: 1.26x faster                                                       |
| pylint                     | 313 ms                                                 | 262 ms: 1.19x faster                                                       |
| go                         | 144 ms                                                 | 122 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.74 us: 1.17x faster                                                      |
| async_tree_none_tg         | 321 ms                                                 | 276 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 504 ms: 1.14x faster                                                       |
| telco                      | 8.54 ms                                                | 7.70 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 493 ms: 1.11x faster                                                       |
| json                       | 5.36 ms                                                | 4.85 ms: 1.11x faster                                                      |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                      |
| generators                 | 29.0 ms                                                | 26.7 ms: 1.08x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                     |
| k_core                     | 2.35 sec                                               | 2.20 sec: 1.07x faster                                                     |
| genshi_text                | 23.5 ms                                                | 22.1 ms: 1.06x faster                                                      |
| richards                   | 48.7 ms                                                | 45.8 ms: 1.06x faster                                                      |
| regex_v8                   | 26.2 ms                                                | 24.9 ms: 1.05x faster                                                      |
| richards_super             | 54.9 ms                                                | 52.2 ms: 1.05x faster                                                      |
| logging_format             | 6.40 us                                                | 6.10 us: 1.05x faster                                                      |
| crypto_pyaes               | 75.3 ms                                                | 71.9 ms: 1.05x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                       |
| tomli_loads                | 2.14 sec                                               | 2.04 sec: 1.05x faster                                                     |
| json_loads                 | 27.2 us                                                | 26.1 us: 1.04x faster                                                      |
| thrift                     | 809 us                                                 | 782 us: 1.03x faster                                                       |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.89 ms: 1.03x faster                                                      |
| logging_simple             | 5.72 us                                                | 5.56 us: 1.03x faster                                                      |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| 2to3                       | 267 ms                                                 | 260 ms: 1.03x faster                                                       |
| python_startup_no_site     | 6.96 ms                                                | 6.79 ms: 1.03x faster                                                      |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.02x faster                                                       |
| typing_runtime_protocols   | 165 us                                                 | 161 us: 1.02x faster                                                       |
| regex_effbot               | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                       |
| django_template            | 35.2 ms                                                | 34.5 ms: 1.02x faster                                                      |
| sympy_str                  | 275 ms                                                 | 271 ms: 1.02x faster                                                       |
| sympy_expand               | 463 ms                                                 | 457 ms: 1.01x faster                                                       |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                      |
| connected_components       | 444 ms                                                 | 439 ms: 1.01x faster                                                       |
| async_generators           | 436 ms                                                 | 431 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                     |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.01x faster                                                       |
| regex_dna                  | 218 ms                                                 | 217 ms: 1.01x faster                                                       |
| python_startup             | 12.5 ms                                                | 12.4 ms: 1.00x faster                                                      |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                      |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.00x slower                                                       |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                       |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| xml_etree_generate         | 86.7 ms                                                | 87.2 ms: 1.01x slower                                                      |
| docutils                   | 2.59 sec                                               | 2.61 sec: 1.01x slower                                                     |
| xml_etree_process          | 60.6 ms                                                | 61.2 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 53.7 ms                                                | 54.4 ms: 1.01x slower                                                      |
| genshi_xml                 | 50.9 ms                                                | 51.6 ms: 1.01x slower                                                      |
| scimark_fft                | 364 ms                                                 | 370 ms: 1.02x slower                                                       |
| pyflate                    | 471 ms                                                 | 479 ms: 1.02x slower                                                       |
| html5lib                   | 64.2 ms                                                | 65.4 ms: 1.02x slower                                                      |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                       |
| raytrace                   | 267 ms                                                 | 273 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 67.4 ms                                                | 69.0 ms: 1.02x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                      |
| scimark_sor                | 124 ms                                                 | 127 ms: 1.03x slower                                                       |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                       |
| bpe_tokeniser              | 4.75 sec                                               | 4.88 sec: 1.03x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                                      |
| bench_thread_pool          | 822 us                                                 | 851 us: 1.04x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                      |
| nqueens                    | 78.4 ms                                                | 82.1 ms: 1.05x slower                                                      |
| deltablue                  | 3.23 ms                                                | 3.40 ms: 1.05x slower                                                      |
| chaos                      | 58.1 ms                                                | 61.2 ms: 1.05x slower                                                      |
| mako                       | 11.1 ms                                                | 11.7 ms: 1.05x slower                                                      |
| pickle_pure_python         | 310 us                                                 | 328 us: 1.06x slower                                                       |
| float                      | 79.2 ms                                                | 83.9 ms: 1.06x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                      |
| xml_etree_parse            | 156 ms                                                 | 172 ms: 1.11x slower                                                       |
| nbody                      | 87.0 ms                                                | 98.4 ms: 1.13x slower                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 120 ms: 1.19x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 84.3 ms: 3.52x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (7): shortest_path, coverage, hexiom, dulwich_log, mdp, pprint_safe_repr, fannkuch
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241113-3.14.0a1+-47eb1b5/bm-20241113-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-47eb1b5.json: sqlite_synth

- Geometric mean (including insignificant results): 1.049x faster
# HPT report

- Reliability score: 99.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x
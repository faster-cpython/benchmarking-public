# Results vs. 3.13.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: a94d30d
- commit date: 2024-11-09
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 258 ms: 1.03x faster                                                       |
| docutils       | 2.59 sec                                               | 2.61 sec: 1.01x slower                                                     |
| html5lib       | 64.2 ms                                                | 62.7 ms: 1.02x faster                                                      |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 319 ms: 1.45x faster                                                       |
| async_tree_none            | 351 ms                                                 | 258 ms: 1.36x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 327 ms: 1.35x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 640 ms: 1.34x faster                                                       |
| async_tree_io              | 842 ms                                                 | 629 ms: 1.34x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 246 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 496 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 477 ms: 1.14x faster                                                       |
| async_generators           | 436 ms                                                 | 427 ms: 1.02x faster                                                       |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                       |
| nbody          | 87.0 ms                                                | 95.1 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                      |
| regex_effbot   | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                      |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                       |
| json_loads           | 27.2 us                                                | 26.0 us: 1.05x faster                                                      |
| xml_etree_process    | 60.6 ms                                                | 58.9 ms: 1.03x faster                                                      |
| xml_etree_generate   | 86.7 ms                                                | 84.6 ms: 1.02x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 2.11 sec: 1.02x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 99.7 ms: 1.01x faster                                                      |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                       |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                      |
| pickle_pure_python   | 310 us                                                 | 328 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 6.78 ms: 1.03x faster                                                      |
| python_startup         | 12.5 ms                                                | 12.3 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.1 ms: 1.06x faster                                                      |
| genshi_xml      | 50.9 ms                                                | 50.2 ms: 1.01x faster                                                      |
| django_template | 35.2 ms                                                | 34.9 ms: 1.01x faster                                                      |
| mako            | 11.1 ms                                                | 11.8 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 4.37 ms                                                | 1.97 ms: 2.22x faster                                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 319 ms: 1.45x faster                                                       |
| create_gc_cycles           | 2.41 ms                                                | 1.70 ms: 1.41x faster                                                      |
| deepcopy                   | 358 us                                                 | 262 us: 1.37x faster                                                       |
| async_tree_none            | 351 ms                                                 | 258 ms: 1.36x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 327 ms: 1.35x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 640 ms: 1.34x faster                                                       |
| async_tree_io              | 842 ms                                                 | 629 ms: 1.34x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 246 ms: 1.30x faster                                                       |
| deepcopy_memo              | 39.1 us                                                | 30.7 us: 1.28x faster                                                      |
| pylint                     | 313 ms                                                 | 261 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.68 us: 1.20x faster                                                      |
| go                         | 144 ms                                                 | 121 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 496 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 477 ms: 1.14x faster                                                       |
| json                       | 5.36 ms                                                | 4.79 ms: 1.12x faster                                                      |
| telco                      | 8.54 ms                                                | 7.77 ms: 1.10x faster                                                      |
| mdp                        | 2.72 sec                                               | 2.52 sec: 1.08x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.3 ms: 1.08x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                                       |
| genshi_text                | 23.5 ms                                                | 22.1 ms: 1.06x faster                                                      |
| richards                   | 48.7 ms                                                | 45.9 ms: 1.06x faster                                                      |
| generators                 | 29.0 ms                                                | 27.4 ms: 1.06x faster                                                      |
| regex_v8                   | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                      |
| logging_format             | 6.40 us                                                | 6.06 us: 1.05x faster                                                      |
| thrift                     | 809 us                                                 | 768 us: 1.05x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                       |
| json_loads                 | 27.2 us                                                | 26.0 us: 1.05x faster                                                      |
| richards_super             | 54.9 ms                                                | 52.6 ms: 1.04x faster                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.56 sec: 1.04x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.52 us: 1.04x faster                                                      |
| regex_effbot               | 3.73 ms                                                | 3.61 ms: 1.03x faster                                                      |
| 2to3                       | 267 ms                                                 | 258 ms: 1.03x faster                                                       |
| typing_runtime_protocols   | 165 us                                                 | 159 us: 1.03x faster                                                       |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.5 ms: 1.03x faster                                                      |
| crypto_pyaes               | 75.3 ms                                                | 73.0 ms: 1.03x faster                                                      |
| xml_etree_process          | 60.6 ms                                                | 58.9 ms: 1.03x faster                                                      |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                     |
| python_startup_no_site     | 6.96 ms                                                | 6.78 ms: 1.03x faster                                                      |
| k_core                     | 2.35 sec                                               | 2.29 sec: 1.03x faster                                                     |
| xml_etree_generate         | 86.7 ms                                                | 84.6 ms: 1.02x faster                                                      |
| html5lib                   | 64.2 ms                                                | 62.7 ms: 1.02x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                       |
| async_generators           | 436 ms                                                 | 427 ms: 1.02x faster                                                       |
| sympy_str                  | 275 ms                                                 | 269 ms: 1.02x faster                                                       |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                       |
| tomli_loads                | 2.14 sec                                               | 2.11 sec: 1.02x faster                                                     |
| sympy_expand               | 463 ms                                                 | 457 ms: 1.02x faster                                                       |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 99.7 ms: 1.01x faster                                                      |
| genshi_xml                 | 50.9 ms                                                | 50.2 ms: 1.01x faster                                                      |
| python_startup             | 12.5 ms                                                | 12.3 ms: 1.01x faster                                                      |
| pyflate                    | 471 ms                                                 | 466 ms: 1.01x faster                                                       |
| django_template            | 35.2 ms                                                | 34.9 ms: 1.01x faster                                                      |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                      |
| docutils                   | 2.59 sec                                               | 2.61 sec: 1.01x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 108 ms                                                 | 108 ms: 1.01x slower                                                       |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                       |
| dulwich_log                | 64.3 ms                                                | 65.2 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 68.6 ms: 1.02x slower                                                      |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.62 ms: 1.02x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.17 ms: 1.03x slower                                                      |
| raytrace                   | 267 ms                                                 | 275 ms: 1.03x slower                                                       |
| deltablue                  | 3.23 ms                                                | 3.32 ms: 1.03x slower                                                      |
| scimark_lu                 | 113 ms                                                 | 116 ms: 1.03x slower                                                       |
| scimark_sor                | 124 ms                                                 | 127 ms: 1.03x slower                                                       |
| hexiom                     | 6.16 ms                                                | 6.37 ms: 1.03x slower                                                      |
| nqueens                    | 78.4 ms                                                | 81.2 ms: 1.04x slower                                                      |
| bench_thread_pool          | 822 us                                                 | 852 us: 1.04x slower                                                       |
| scimark_fft                | 364 ms                                                 | 380 ms: 1.04x slower                                                       |
| logging_silent             | 102 ns                                                 | 106 ns: 1.04x slower                                                       |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                      |
| pickle_pure_python         | 310 us                                                 | 328 us: 1.06x slower                                                       |
| chaos                      | 58.1 ms                                                | 61.5 ms: 1.06x slower                                                      |
| mako                       | 11.1 ms                                                | 11.8 ms: 1.06x slower                                                      |
| nbody                      | 87.0 ms                                                | 95.1 ms: 1.09x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.7 ms: 3.36x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (10): shortest_path, connected_components, regex_dna, pprint_pformat, pprint_safe_repr, float, asyncio_websockets, fannkuch, spectral_norm, coverage
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241109-3.14.0a1+-a94d30d/bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d.json: sqlite_synth

- Geometric mean (including insignificant results): 1.058x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x
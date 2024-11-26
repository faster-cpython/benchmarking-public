# Results vs. 3.13.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: fb5fdad
- commit date: 2024-11-10
- overall geometric mean: 1.053x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 258 ms: 1.03x faster                                                       |
| docutils       | 2.59 sec                                               | 2.62 sec: 1.01x slower                                                     |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 320 ms: 1.45x faster                                                       |
| async_tree_none            | 351 ms                                                 | 259 ms: 1.35x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 637 ms: 1.34x faster                                                       |
| async_tree_io              | 842 ms                                                 | 627 ms: 1.34x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 337 ms: 1.31x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 247 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 488 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 466 ms: 1.17x faster                                                       |
| async_generators           | 436 ms                                                 | 429 ms: 1.02x faster                                                       |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 78.8 ms: 1.01x faster                                                      |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                       |
| nbody          | 87.0 ms                                                | 96.3 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                      |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                       |
| regex_effbot   | 3.73 ms                                                | 3.72 ms: 1.00x faster                                                      |
| regex_dna      | 218 ms                                                 | 222 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 144 ms: 1.08x faster                                                       |
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                     |
| xml_etree_process    | 60.6 ms                                                | 59.1 ms: 1.03x faster                                                      |
| xml_etree_generate   | 86.7 ms                                                | 84.8 ms: 1.02x faster                                                      |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 99.9 ms: 1.01x faster                                                      |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                                       |
| pickle_pure_python   | 310 us                                                 | 330 us: 1.06x slower                                                       |
| json_dumps           | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 6.83 ms: 1.02x faster                                                      |
| python_startup         | 12.5 ms                                                | 12.4 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.3 ms: 1.06x faster                                                      |
| genshi_xml      | 50.9 ms                                                | 50.3 ms: 1.01x faster                                                      |
| django_template | 35.2 ms                                                | 35.0 ms: 1.00x faster                                                      |
| mako            | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 4.37 ms                                                | 1.89 ms: 2.31x faster                                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 320 ms: 1.45x faster                                                       |
| deepcopy                   | 358 us                                                 | 262 us: 1.37x faster                                                       |
| create_gc_cycles           | 2.41 ms                                                | 1.77 ms: 1.36x faster                                                      |
| async_tree_none            | 351 ms                                                 | 259 ms: 1.35x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 637 ms: 1.34x faster                                                       |
| async_tree_io              | 842 ms                                                 | 627 ms: 1.34x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 337 ms: 1.31x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 247 ms: 1.30x faster                                                       |
| deepcopy_memo              | 39.1 us                                                | 30.6 us: 1.28x faster                                                      |
| pylint                     | 313 ms                                                 | 263 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.70 us: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 488 ms: 1.18x faster                                                       |
| go                         | 144 ms                                                 | 122 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 466 ms: 1.17x faster                                                       |
| telco                      | 8.54 ms                                                | 7.75 ms: 1.10x faster                                                      |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                      |
| json                       | 5.36 ms                                                | 4.95 ms: 1.08x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 144 ms: 1.08x faster                                                       |
| mdp                        | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                     |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                      |
| generators                 | 29.0 ms                                                | 27.4 ms: 1.06x faster                                                      |
| genshi_text                | 23.5 ms                                                | 22.3 ms: 1.06x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                       |
| thrift                     | 809 us                                                 | 774 us: 1.04x faster                                                       |
| richards                   | 48.7 ms                                                | 46.6 ms: 1.04x faster                                                      |
| logging_format             | 6.40 us                                                | 6.14 us: 1.04x faster                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.58 sec: 1.04x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                     |
| richards_super             | 54.9 ms                                                | 53.0 ms: 1.03x faster                                                      |
| 2to3                       | 267 ms                                                 | 258 ms: 1.03x faster                                                       |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                     |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                     |
| k_core                     | 2.35 sec                                               | 2.29 sec: 1.03x faster                                                     |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                      |
| xml_etree_process          | 60.6 ms                                                | 59.1 ms: 1.03x faster                                                      |
| logging_simple             | 5.72 us                                                | 5.58 us: 1.03x faster                                                      |
| xml_etree_generate         | 86.7 ms                                                | 84.8 ms: 1.02x faster                                                      |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                      |
| python_startup_no_site     | 6.96 ms                                                | 6.83 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.02x faster                                                       |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                       |
| async_generators           | 436 ms                                                 | 429 ms: 1.02x faster                                                       |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 99.9 ms: 1.01x faster                                                      |
| genshi_xml                 | 50.9 ms                                                | 50.3 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.99 ms: 1.01x faster                                                      |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                       |
| connected_components       | 444 ms                                                 | 440 ms: 1.01x faster                                                       |
| sympy_str                  | 275 ms                                                 | 273 ms: 1.01x faster                                                       |
| python_startup             | 12.5 ms                                                | 12.4 ms: 1.01x faster                                                      |
| float                      | 79.2 ms                                                | 78.8 ms: 1.01x faster                                                      |
| django_template            | 35.2 ms                                                | 35.0 ms: 1.00x faster                                                      |
| regex_effbot               | 3.73 ms                                                | 3.72 ms: 1.00x faster                                                      |
| pprint_pformat             | 1.49 sec                                               | 1.50 sec: 1.00x slower                                                     |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                                       |
| docutils                   | 2.59 sec                                               | 2.62 sec: 1.01x slower                                                     |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 728 ms                                                 | 738 ms: 1.01x slower                                                       |
| regex_dna                  | 218 ms                                                 | 222 ms: 1.01x slower                                                       |
| dulwich_log                | 64.3 ms                                                | 65.3 ms: 1.01x slower                                                      |
| coverage                   | 84.0 ms                                                | 85.4 ms: 1.02x slower                                                      |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                                      |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 69.9 ms: 1.04x slower                                                      |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                      |
| hexiom                     | 6.16 ms                                                | 6.40 ms: 1.04x slower                                                      |
| bench_thread_pool          | 822 us                                                 | 856 us: 1.04x slower                                                       |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                      |
| raytrace                   | 267 ms                                                 | 278 ms: 1.04x slower                                                       |
| deltablue                  | 3.23 ms                                                | 3.37 ms: 1.05x slower                                                      |
| nqueens                    | 78.4 ms                                                | 82.9 ms: 1.06x slower                                                      |
| chaos                      | 58.1 ms                                                | 61.5 ms: 1.06x slower                                                      |
| pickle_pure_python         | 310 us                                                 | 330 us: 1.06x slower                                                       |
| json_dumps                 | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                      |
| scimark_sor                | 124 ms                                                 | 134 ms: 1.08x slower                                                       |
| logging_silent             | 102 ns                                                 | 110 ns: 1.08x slower                                                       |
| nbody                      | 87.0 ms                                                | 96.3 ms: 1.11x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.43x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (11): sqlglot_optimize, shortest_path, pyflate, sympy_expand, sympy_integrate, scimark_fft, crypto_pyaes, asyncio_websockets, fannkuch, sqlglot_normalize, html5lib
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241110-3.14.0a1+-fb5fdad/bm-20241110-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-fb5fdad.json: sqlite_synth

- Geometric mean (including insignificant results): 1.053x faster
# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x
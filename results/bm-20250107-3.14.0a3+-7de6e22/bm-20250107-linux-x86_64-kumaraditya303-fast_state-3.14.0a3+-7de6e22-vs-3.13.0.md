# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.039x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                 |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                               |
| html5lib       | 63.4 ms                                                | 60.9 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 298 ms: 1.56x faster                                                 |
| async_tree_io              | 838 ms                                                 | 577 ms: 1.45x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 594 ms: 1.45x faster                                                 |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 484 ms: 1.18x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 467 ms: 1.16x faster                                                 |
| async_generators           | 433 ms                                                 | 420 ms: 1.03x faster                                                 |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.6 ms: 1.07x faster                                                |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| nbody          | 87.7 ms                                                | 97.2 ms: 1.11x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                 |
| regex_v8       | 26.9 ms                                                | 26.4 ms: 1.02x faster                                                |
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                 |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.05x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 96.6 ms: 1.05x faster                                                |
| json_loads           | 27.2 us                                                | 26.4 us: 1.03x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 84.8 ms: 1.02x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 59.6 ms: 1.01x faster                                                |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                 |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                |
| mako            | 10.7 ms                                                | 11.8 ms: 1.11x slower                                                |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 298 ms: 1.56x faster                                                 |
| async_tree_io              | 838 ms                                                 | 577 ms: 1.45x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 594 ms: 1.45x faster                                                 |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                 |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.62 us: 1.24x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 31.3 us: 1.23x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 484 ms: 1.18x faster                                                 |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 467 ms: 1.16x faster                                                 |
| pylint                     | 312 ms                                                 | 277 ms: 1.12x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                                 |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.08x faster                                                |
| telco                      | 8.40 ms                                                | 7.84 ms: 1.07x faster                                                |
| json                       | 5.32 ms                                                | 4.97 ms: 1.07x faster                                                |
| float                      | 78.7 ms                                                | 73.6 ms: 1.07x faster                                                |
| scimark_fft                | 367 ms                                                 | 345 ms: 1.06x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 70.4 ms: 1.06x faster                                                |
| richards                   | 47.5 ms                                                | 44.9 ms: 1.06x faster                                                |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.05x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 96.6 ms: 1.05x faster                                                |
| richards_super             | 53.7 ms                                                | 51.3 ms: 1.05x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.81 ms: 1.05x faster                                                |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.04x faster                                                 |
| thrift                     | 800 us                                                 | 769 us: 1.04x faster                                                 |
| html5lib                   | 63.4 ms                                                | 60.9 ms: 1.04x faster                                                |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.04x faster                                               |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                 |
| async_generators           | 433 ms                                                 | 420 ms: 1.03x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                 |
| json_loads                 | 27.2 us                                                | 26.4 us: 1.03x faster                                                |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                |
| pyflate                    | 470 ms                                                 | 458 ms: 1.02x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 84.8 ms: 1.02x faster                                                |
| genshi_text                | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.85 us: 1.02x faster                                                |
| sqlglot_optimize           | 53.4 ms                                                | 52.6 ms: 1.02x faster                                                |
| regex_v8                   | 26.9 ms                                                | 26.4 ms: 1.02x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 59.6 ms: 1.01x faster                                                |
| generators                 | 28.8 ms                                                | 28.4 ms: 1.01x faster                                                |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                                 |
| connected_components       | 447 ms                                                 | 441 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 63.9 ms: 1.01x faster                                                |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                                |
| gc_traversal               | 4.90 ms                                                | 4.93 ms: 1.01x slower                                                |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                |
| python_startup_no_site     | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                               |
| nqueens                    | 80.9 ms                                                | 82.0 ms: 1.01x slower                                                |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.01x slower                                                 |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.02x slower                                                 |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 68.2 ms: 1.02x slower                                                |
| fannkuch                   | 394 ms                                                 | 404 ms: 1.03x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.30 ms: 1.03x slower                                                |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.31 ms: 1.04x slower                                                |
| chaos                      | 58.0 ms                                                | 60.7 ms: 1.05x slower                                                |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.06x slower                                                |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 866 us: 1.06x slower                                                 |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                 |
| many_optionals             | 857 us                                                 | 942 us: 1.10x slower                                                 |
| mako                       | 10.7 ms                                                | 11.8 ms: 1.11x slower                                                |
| nbody                      | 87.7 ms                                                | 97.2 ms: 1.11x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.41x slower                                                |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (11): sphinx, mdp, pprint_safe_repr, coverage, logging_format, asyncio_websockets, meteor_contest, logging_simple, sympy_expand, pprint_pformat, sqlglot_parse
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: mypy2

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x
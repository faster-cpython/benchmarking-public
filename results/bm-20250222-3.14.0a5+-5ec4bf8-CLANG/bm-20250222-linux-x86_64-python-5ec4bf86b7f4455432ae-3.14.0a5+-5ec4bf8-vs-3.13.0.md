# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.074x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 250 ms: 1.06x faster                                                   |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                 |
| html5lib       | 63.4 ms                                                | 59.1 ms: 1.07x faster                                                  |
| sphinx         | 1.03 sec                                               | 985 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 594 ms: 1.45x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                                   |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                   |
| async_tree_none            | 350 ms                                                 | 251 ms: 1.40x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 241 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                                   |
| async_generators           | 433 ms                                                 | 378 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                   |
| coroutines                 | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                  |
| nbody          | 87.7 ms                                                | 89.3 ms: 1.02x slower                                                  |
| pidigits       | 186 ms                                                 | 202 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                 | 194 ms: 1.13x faster                                                   |
| regex_effbot   | 3.77 ms                                                | 3.40 ms: 1.11x faster                                                  |
| regex_compile  | 132 ms                                                 | 124 ms: 1.06x faster                                                   |
| regex_v8       | 26.9 ms                                                | 26.1 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.90 sec: 1.12x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 58.5 ms: 1.03x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.01x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 312 us: 1.03x slower                                                   |
| xml_etree_parse      | 154 ms                                                 | 162 ms: 1.05x slower                                                   |
| json_loads           | 27.2 us                                                | 30.0 us: 1.11x slower                                                  |
| json_dumps           | 10.1 ms                                                | 12.1 ms: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.99 ms: 1.00x faster                                                  |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 47.8 ms: 1.06x faster                                                  |
| django_template | 31.7 ms                                                | 30.3 ms: 1.04x faster                                                  |
| mako            | 10.7 ms                                                | 11.7 ms: 1.10x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 594 ms: 1.45x faster                                                   |
| deepcopy                   | 354 us                                                 | 247 us: 1.44x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                                   |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                   |
| async_tree_none            | 350 ms                                                 | 251 ms: 1.40x faster                                                   |
| spectral_norm              | 113 ms                                                 | 82.3 ms: 1.38x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 241 ms: 1.32x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.50 us: 1.30x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                                  |
| go                         | 141 ms                                                 | 113 ms: 1.25x faster                                                   |
| scimark_fft                | 367 ms                                                 | 295 ms: 1.24x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.11 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                                   |
| richards                   | 47.5 ms                                                | 40.8 ms: 1.17x faster                                                  |
| float                      | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                  |
| pylint                     | 312 ms                                                 | 270 ms: 1.15x faster                                                   |
| pathlib                    | 17.4 ms                                                | 15.1 ms: 1.15x faster                                                  |
| telco                      | 8.40 ms                                                | 7.31 ms: 1.15x faster                                                  |
| async_generators           | 433 ms                                                 | 378 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                   |
| regex_dna                  | 220 ms                                                 | 194 ms: 1.13x faster                                                   |
| richards_super             | 53.7 ms                                                | 47.6 ms: 1.13x faster                                                  |
| scimark_sor                | 122 ms                                                 | 109 ms: 1.12x faster                                                   |
| logging_silent             | 101 ns                                                 | 90.3 ns: 1.12x faster                                                  |
| pyflate                    | 470 ms                                                 | 420 ms: 1.12x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.90 sec: 1.12x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.40 ms: 1.11x faster                                                  |
| typing_runtime_protocols   | 160 us                                                 | 146 us: 1.10x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.65 us: 1.10x faster                                                  |
| nqueens                    | 80.9 ms                                                | 73.9 ms: 1.09x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 61.8 ms: 1.08x faster                                                  |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.35 sec: 1.08x faster                                                 |
| thrift                     | 800 us                                                 | 742 us: 1.08x faster                                                   |
| deltablue                  | 3.19 ms                                                | 2.98 ms: 1.07x faster                                                  |
| html5lib                   | 63.4 ms                                                | 59.1 ms: 1.07x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                 |
| comprehensions             | 16.5 us                                                | 15.5 us: 1.06x faster                                                  |
| 2to3                       | 266 ms                                                 | 250 ms: 1.06x faster                                                   |
| chaos                      | 58.0 ms                                                | 54.6 ms: 1.06x faster                                                  |
| regex_compile              | 132 ms                                                 | 124 ms: 1.06x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 125 ms: 1.06x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 142 ms: 1.06x faster                                                   |
| sympy_str                  | 273 ms                                                 | 258 ms: 1.06x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 47.8 ms: 1.06x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.1 ms: 1.05x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.37 us: 1.05x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| logging_format             | 6.23 us                                                | 5.94 us: 1.05x faster                                                  |
| sphinx                     | 1.03 sec                                               | 985 ms: 1.05x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.21 ms: 1.05x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.05x faster                                                 |
| django_template            | 31.7 ms                                                | 30.3 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.51 ms: 1.04x faster                                                  |
| coverage                   | 82.8 ms                                                | 79.8 ms: 1.04x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 71.9 ms: 1.04x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 62.2 ms: 1.04x faster                                                  |
| scimark_lu                 | 114 ms                                                 | 110 ms: 1.04x faster                                                   |
| sympy_expand               | 456 ms                                                 | 441 ms: 1.03x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 58.5 ms: 1.03x faster                                                  |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 51.8 ms: 1.03x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 26.1 ms: 1.03x faster                                                  |
| hexiom                     | 6.08 ms                                                | 5.94 ms: 1.02x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                  |
| coroutines                 | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                  |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                                   |
| raytrace                   | 262 ms                                                 | 259 ms: 1.01x faster                                                   |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.99 ms: 1.00x faster                                                  |
| fannkuch                   | 394 ms                                                 | 395 ms: 1.00x slower                                                   |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.00x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 821 us: 1.00x slower                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.01x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 737 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.02x slower                                                 |
| nbody                      | 87.7 ms                                                | 89.3 ms: 1.02x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 5.01 ms: 1.02x slower                                                  |
| meteor_contest             | 108 ms                                                 | 111 ms: 1.02x slower                                                   |
| json                       | 5.32 ms                                                | 5.45 ms: 1.02x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 312 us: 1.03x slower                                                   |
| xml_etree_parse            | 154 ms                                                 | 162 ms: 1.05x slower                                                   |
| many_optionals             | 857 us                                                 | 917 us: 1.07x slower                                                   |
| pidigits                   | 186 ms                                                 | 202 ms: 1.08x slower                                                   |
| mdp                        | 2.54 sec                                               | 2.77 sec: 1.09x slower                                                 |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.10x slower                                                  |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.11x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 12.1 ms: 1.19x slower                                                  |
| subparsers                 | 15.5 ms                                                | 19.9 ms: 1.29x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.0 ms: 3.33x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, connected_components
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.074x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.03x
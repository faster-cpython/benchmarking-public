# Results vs. 3.13.0

- fork: python
- ref: cfbc841ef3c27b3e65d1
- machine: linux-x86_64
- commit hash: cfbc841
- commit date: 2024-09-03
- overall geometric mean: 1.030x faster
- HPT reliability: 81.14%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 275 ms: 1.03x slower                                                  |
| docutils       | 2.59 sec                                               | 3.03 sec: 1.17x slower                                                |
| html5lib       | 64.2 ms                                                | 64.7 ms: 1.01x slower                                                 |
| tornado_http   | 92.4 ms                                                | 95.6 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 405 ms: 1.14x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                  |
| async_tree_none           | 351 ms                                                 | 326 ms: 1.08x faster                                                  |
| async_tree_none_tg        | 321 ms                                                 | 313 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 571 ms: 1.01x faster                                                  |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                  |
| async_tree_io_tg          | 857 ms                                                 | 900 ms: 1.05x slower                                                  |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                                  |
| async_tree_io             | 842 ms                                                 | 932 ms: 1.11x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.2 ms: 1.13x faster                                                 |
| nbody          | 87.0 ms                                                | 79.1 ms: 1.10x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.55 ms: 1.05x faster                                                 |
| regex_compile  | 132 ms                                                 | 142 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.8 ms: 1.11x faster                                                 |
| tomli_loads          | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                |
| xml_etree_process    | 60.6 ms                                                | 55.2 ms: 1.10x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.0 ms: 1.03x faster                                                 |
| pickle_pure_python   | 310 us                                                 | 301 us: 1.03x faster                                                  |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                 |
| unpickle_pure_python | 216 us                                                 | 216 us: 1.00x slower                                                  |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.77 ms: 1.13x faster                                                 |
| django_template | 35.2 ms                                                | 35.6 ms: 1.01x slower                                                 |
| genshi_text     | 23.5 ms                                                | 24.2 ms: 1.03x slower                                                 |
| genshi_xml      | 50.9 ms                                                | 58.1 ms: 1.14x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 27.3 us: 1.43x faster                                                 |
| create_gc_cycles          | 2.41 ms                                                | 1.75 ms: 1.37x faster                                                 |
| deepcopy                  | 358 us                                                 | 266 us: 1.35x faster                                                  |
| richards                  | 48.7 ms                                                | 39.2 ms: 1.24x faster                                                 |
| gc_traversal              | 4.37 ms                                                | 3.56 ms: 1.23x faster                                                 |
| richards_super            | 54.9 ms                                                | 45.4 ms: 1.21x faster                                                 |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.20 ms: 1.20x faster                                                 |
| scimark_fft               | 364 ms                                                 | 303 ms: 1.20x faster                                                  |
| deepcopy_reduce           | 3.20 us                                                | 2.68 us: 1.19x faster                                                 |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| spectral_norm             | 115 ms                                                 | 99.2 ms: 1.16x faster                                                 |
| async_tree_memoization_tg | 464 ms                                                 | 405 ms: 1.14x faster                                                  |
| crypto_pyaes              | 75.3 ms                                                | 65.9 ms: 1.14x faster                                                 |
| mako                      | 11.1 ms                                                | 9.77 ms: 1.13x faster                                                 |
| float                     | 79.2 ms                                                | 70.2 ms: 1.13x faster                                                 |
| xml_etree_generate        | 86.7 ms                                                | 77.8 ms: 1.11x faster                                                 |
| tomli_loads               | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                |
| go                        | 144 ms                                                 | 130 ms: 1.10x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                  |
| pathlib                   | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                 |
| nbody                     | 87.0 ms                                                | 79.1 ms: 1.10x faster                                                 |
| xml_etree_process         | 60.6 ms                                                | 55.2 ms: 1.10x faster                                                 |
| telco                     | 8.54 ms                                                | 7.82 ms: 1.09x faster                                                 |
| fannkuch                  | 404 ms                                                 | 372 ms: 1.09x faster                                                  |
| async_tree_none           | 351 ms                                                 | 326 ms: 1.08x faster                                                  |
| scimark_monte_carlo       | 67.4 ms                                                | 62.8 ms: 1.07x faster                                                 |
| bpe_tokeniser             | 4.75 sec                                               | 4.43 sec: 1.07x faster                                                |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.07x faster                                                  |
| mdp                       | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                |
| scimark_sor               | 124 ms                                                 | 116 ms: 1.06x faster                                                  |
| regex_v8                  | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                 |
| regex_effbot              | 3.73 ms                                                | 3.55 ms: 1.05x faster                                                 |
| pyflate                   | 471 ms                                                 | 452 ms: 1.04x faster                                                  |
| thrift                    | 809 us                                                 | 781 us: 1.04x faster                                                  |
| xml_etree_iterparse       | 101 ms                                                 | 98.0 ms: 1.03x faster                                                 |
| pickle_pure_python        | 310 us                                                 | 301 us: 1.03x faster                                                  |
| scimark_lu                | 113 ms                                                 | 109 ms: 1.03x faster                                                  |
| logging_format            | 6.40 us                                                | 6.21 us: 1.03x faster                                                 |
| meteor_contest            | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| json_dumps                | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                 |
| pycparser                 | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                |
| async_tree_none_tg        | 321 ms                                                 | 313 ms: 1.02x faster                                                  |
| deltablue                 | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                 |
| typing_runtime_protocols  | 165 us                                                 | 163 us: 1.01x faster                                                  |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 571 ms: 1.01x faster                                                  |
| unpickle_pure_python      | 216 us                                                 | 216 us: 1.00x slower                                                  |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                  |
| html5lib                  | 64.2 ms                                                | 64.7 ms: 1.01x slower                                                 |
| chaos                     | 58.1 ms                                                | 58.7 ms: 1.01x slower                                                 |
| comprehensions            | 16.5 us                                                | 16.7 us: 1.01x slower                                                 |
| django_template           | 35.2 ms                                                | 35.6 ms: 1.01x slower                                                 |
| pprint_pformat            | 1.49 sec                                               | 1.52 sec: 1.02x slower                                                |
| bench_thread_pool         | 822 us                                                 | 836 us: 1.02x slower                                                  |
| python_startup_no_site    | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                 |
| logging_silent            | 102 ns                                                 | 104 ns: 1.02x slower                                                  |
| raytrace                  | 267 ms                                                 | 274 ms: 1.02x slower                                                  |
| genshi_text               | 23.5 ms                                                | 24.2 ms: 1.03x slower                                                 |
| coverage                  | 84.0 ms                                                | 86.5 ms: 1.03x slower                                                 |
| 2to3                      | 267 ms                                                 | 275 ms: 1.03x slower                                                  |
| tornado_http              | 92.4 ms                                                | 95.6 ms: 1.03x slower                                                 |
| json                      | 5.36 ms                                                | 5.56 ms: 1.04x slower                                                 |
| sqlglot_normalize         | 108 ms                                                 | 113 ms: 1.05x slower                                                  |
| json_loads                | 27.2 us                                                | 28.6 us: 1.05x slower                                                 |
| async_tree_io_tg          | 857 ms                                                 | 900 ms: 1.05x slower                                                  |
| sqlglot_parse             | 1.27 ms                                                | 1.34 ms: 1.05x slower                                                 |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                                  |
| dulwich_log               | 64.3 ms                                                | 68.8 ms: 1.07x slower                                                 |
| sqlglot_transpile         | 1.58 ms                                                | 1.70 ms: 1.07x slower                                                 |
| regex_compile             | 132 ms                                                 | 142 ms: 1.07x slower                                                  |
| sqlglot_optimize          | 53.7 ms                                                | 57.7 ms: 1.07x slower                                                 |
| sympy_expand              | 463 ms                                                 | 504 ms: 1.09x slower                                                  |
| nqueens                   | 78.4 ms                                                | 85.2 ms: 1.09x slower                                                 |
| sympy_str                 | 275 ms                                                 | 299 ms: 1.09x slower                                                  |
| async_tree_io             | 842 ms                                                 | 932 ms: 1.11x slower                                                  |
| hexiom                    | 6.16 ms                                                | 6.85 ms: 1.11x slower                                                 |
| generators                | 29.0 ms                                                | 32.9 ms: 1.14x slower                                                 |
| sympy_integrate           | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                 |
| genshi_xml                | 50.9 ms                                                | 58.1 ms: 1.14x slower                                                 |
| sympy_sum                 | 150 ms                                                 | 173 ms: 1.15x slower                                                  |
| docutils                  | 2.59 sec                                               | 3.03 sec: 1.17x slower                                                |
| pylint                    | 313 ms                                                 | 372 ms: 1.19x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (6): pprint_safe_repr, logging_simple, bench_mp_pool, regex_dna, coroutines, async_tree_cpu_io_mixed_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240903-3.14.0a0-cfbc841-JIT/bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 81.14% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x
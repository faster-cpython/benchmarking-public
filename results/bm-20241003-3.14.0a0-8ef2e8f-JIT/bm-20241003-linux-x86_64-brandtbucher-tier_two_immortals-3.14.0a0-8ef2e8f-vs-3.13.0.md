# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_immortals
- machine: linux-x86_64
- commit hash: 8ef2e8f
- commit date: 2024-10-03
- overall geometric mean: 1.028x faster
- HPT reliability: 79.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 279 ms: 1.05x slower                                                      |
| docutils       | 2.59 sec                                               | 2.92 sec: 1.12x slower                                                    |
| html5lib       | 64.2 ms                                                | 64.7 ms: 1.01x slower                                                     |
| tornado_http   | 92.4 ms                                                | 94.9 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 387 ms: 1.20x faster                                                      |
| async_tree_none           | 351 ms                                                 | 317 ms: 1.11x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.08x faster                                                      |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.04x faster                                                      |
| coroutines                | 22.7 ms                                                | 22.4 ms: 1.01x faster                                                     |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                      |
| async_generators          | 436 ms                                                 | 452 ms: 1.04x slower                                                      |
| async_tree_io             | 842 ms                                                 | 885 ms: 1.05x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 71.8 ms: 1.10x faster                                                     |
| nbody          | 87.0 ms                                                | 82.3 ms: 1.06x faster                                                     |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                     |
| regex_effbot   | 3.73 ms                                                | 3.69 ms: 1.01x faster                                                     |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                      |
| regex_compile  | 132 ms                                                 | 143 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 76.8 ms: 1.13x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 1.90 sec: 1.13x faster                                                    |
| xml_etree_process    | 60.6 ms                                                | 54.4 ms: 1.11x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.08x faster                                                      |
| json_dumps           | 10.6 ms                                                | 10.2 ms: 1.04x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 98.1 ms: 1.03x faster                                                     |
| unpickle_pure_python | 216 us                                                 | 213 us: 1.01x faster                                                      |
| json_loads           | 27.2 us                                                | 26.9 us: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                     |
| python_startup_no_site | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.90 ms: 1.12x faster                                                     |
| django_template | 35.2 ms                                                | 36.9 ms: 1.05x slower                                                     |
| genshi_text     | 23.5 ms                                                | 25.5 ms: 1.09x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 57.9 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 27.1 us: 1.44x faster                                                     |
| create_gc_cycles          | 2.41 ms                                                | 1.73 ms: 1.39x faster                                                     |
| deepcopy                  | 358 us                                                 | 271 us: 1.32x faster                                                      |
| richards                  | 48.7 ms                                                | 39.5 ms: 1.23x faster                                                     |
| richards_super            | 54.9 ms                                                | 44.7 ms: 1.23x faster                                                     |
| deepcopy_reduce           | 3.20 us                                                | 2.65 us: 1.21x faster                                                     |
| async_tree_memoization_tg | 464 ms                                                 | 387 ms: 1.20x faster                                                      |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                     |
| scimark_fft               | 364 ms                                                 | 307 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.36 ms: 1.16x faster                                                     |
| crypto_pyaes              | 75.3 ms                                                | 65.4 ms: 1.15x faster                                                     |
| spectral_norm             | 115 ms                                                 | 100 ms: 1.15x faster                                                      |
| telco                     | 8.54 ms                                                | 7.49 ms: 1.14x faster                                                     |
| gc_traversal              | 4.37 ms                                                | 3.85 ms: 1.14x faster                                                     |
| xml_etree_generate        | 86.7 ms                                                | 76.8 ms: 1.13x faster                                                     |
| tomli_loads               | 2.14 sec                                               | 1.90 sec: 1.13x faster                                                    |
| pathlib                   | 17.5 ms                                                | 15.6 ms: 1.12x faster                                                     |
| mako                      | 11.1 ms                                                | 9.90 ms: 1.12x faster                                                     |
| xml_etree_process         | 60.6 ms                                                | 54.4 ms: 1.11x faster                                                     |
| async_tree_none           | 351 ms                                                 | 317 ms: 1.11x faster                                                      |
| float                     | 79.2 ms                                                | 71.8 ms: 1.10x faster                                                     |
| go                        | 144 ms                                                 | 132 ms: 1.09x faster                                                      |
| fannkuch                  | 404 ms                                                 | 372 ms: 1.09x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.08x faster                                                      |
| pyflate                   | 471 ms                                                 | 435 ms: 1.08x faster                                                      |
| scimark_monte_carlo       | 67.4 ms                                                | 62.5 ms: 1.08x faster                                                     |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.08x faster                                                      |
| bpe_tokeniser             | 4.75 sec                                               | 4.43 sec: 1.07x faster                                                    |
| mdp                       | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                    |
| json                      | 5.36 ms                                                | 5.06 ms: 1.06x faster                                                     |
| nbody                     | 87.0 ms                                                | 82.3 ms: 1.06x faster                                                     |
| scimark_sor               | 124 ms                                                 | 118 ms: 1.05x faster                                                      |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.04x faster                                                      |
| json_dumps                | 10.6 ms                                                | 10.2 ms: 1.04x faster                                                     |
| xml_etree_iterparse       | 101 ms                                                 | 98.1 ms: 1.03x faster                                                     |
| regex_v8                  | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                     |
| scimark_lu                | 113 ms                                                 | 110 ms: 1.02x faster                                                      |
| logging_format            | 6.40 us                                                | 6.28 us: 1.02x faster                                                     |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.02x faster                                                      |
| thrift                    | 809 us                                                 | 797 us: 1.02x faster                                                      |
| unpickle_pure_python      | 216 us                                                 | 213 us: 1.01x faster                                                      |
| json_loads                | 27.2 us                                                | 26.9 us: 1.01x faster                                                     |
| coroutines                | 22.7 ms                                                | 22.4 ms: 1.01x faster                                                     |
| deltablue                 | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                     |
| regex_effbot              | 3.73 ms                                                | 3.69 ms: 1.01x faster                                                     |
| logging_simple            | 5.72 us                                                | 5.67 us: 1.01x faster                                                     |
| pidigits                  | 186 ms                                                 | 185 ms: 1.01x faster                                                      |
| html5lib                  | 64.2 ms                                                | 64.7 ms: 1.01x slower                                                     |
| python_startup_no_site    | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                     |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                      |
| regex_dna                 | 218 ms                                                 | 221 ms: 1.01x slower                                                      |
| pprint_safe_repr          | 728 ms                                                 | 740 ms: 1.02x slower                                                      |
| comprehensions            | 16.5 us                                                | 16.8 us: 1.02x slower                                                     |
| coverage                  | 84.0 ms                                                | 85.8 ms: 1.02x slower                                                     |
| logging_silent            | 102 ns                                                 | 104 ns: 1.02x slower                                                      |
| tornado_http              | 92.4 ms                                                | 94.9 ms: 1.03x slower                                                     |
| chaos                     | 58.1 ms                                                | 59.7 ms: 1.03x slower                                                     |
| async_generators          | 436 ms                                                 | 452 ms: 1.04x slower                                                      |
| pprint_pformat            | 1.49 sec                                               | 1.55 sec: 1.04x slower                                                    |
| raytrace                  | 267 ms                                                 | 278 ms: 1.04x slower                                                      |
| 2to3                      | 267 ms                                                 | 279 ms: 1.05x slower                                                      |
| django_template           | 35.2 ms                                                | 36.9 ms: 1.05x slower                                                     |
| async_tree_io             | 842 ms                                                 | 885 ms: 1.05x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                     |
| dulwich_log               | 64.3 ms                                                | 68.2 ms: 1.06x slower                                                     |
| sqlglot_transpile         | 1.58 ms                                                | 1.68 ms: 1.06x slower                                                     |
| sqlglot_normalize         | 108 ms                                                 | 114 ms: 1.06x slower                                                      |
| regex_compile             | 132 ms                                                 | 143 ms: 1.08x slower                                                      |
| genshi_text               | 23.5 ms                                                | 25.5 ms: 1.09x slower                                                     |
| sympy_expand              | 463 ms                                                 | 505 ms: 1.09x slower                                                      |
| bench_thread_pool         | 822 us                                                 | 896 us: 1.09x slower                                                      |
| nqueens                   | 78.4 ms                                                | 85.9 ms: 1.10x slower                                                     |
| sympy_str                 | 275 ms                                                 | 303 ms: 1.10x slower                                                      |
| sqlglot_optimize          | 53.7 ms                                                | 60.3 ms: 1.12x slower                                                     |
| docutils                  | 2.59 sec                                               | 2.92 sec: 1.12x slower                                                    |
| hexiom                    | 6.16 ms                                                | 6.95 ms: 1.13x slower                                                     |
| genshi_xml                | 50.9 ms                                                | 57.9 ms: 1.14x slower                                                     |
| sympy_sum                 | 150 ms                                                 | 175 ms: 1.16x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 23.4 ms: 1.18x slower                                                     |
| generators                | 29.0 ms                                                | 34.5 ms: 1.19x slower                                                     |
| pylint                    | 313 ms                                                 | 374 ms: 1.20x slower                                                      |
| bench_mp_pool             | 24.0 ms                                                | 60.2 ms: 2.51x slower                                                     |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, pickle_pure_python, pycparser, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, async_tree_io_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241003-3.14.0a0-8ef2e8f-JIT/bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 79.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x
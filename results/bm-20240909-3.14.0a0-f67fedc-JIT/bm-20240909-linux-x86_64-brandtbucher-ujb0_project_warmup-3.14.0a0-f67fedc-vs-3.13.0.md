# Results vs. 3.13.0

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: f67fedc
- commit date: 2024-09-09
- overall geometric mean: 1.021x slower
- HPT reliability: 94.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 292 ms: 1.09x slower                                                       |
| docutils       | 2.59 sec                                               | 3.47 sec: 1.34x slower                                                     |
| html5lib       | 64.2 ms                                                | 70.6 ms: 1.10x slower                                                      |
| tornado_http   | 92.4 ms                                                | 119 ms: 1.29x slower                                                       |
| Geometric mean | (ref)                                                  | 1.20x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 409 ms: 1.13x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 422 ms: 1.05x faster                                                       |
| async_tree_none           | 351 ms                                                 | 339 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 571 ms: 1.01x faster                                                       |
| asyncio_websockets        | 552 ms                                                 | 557 ms: 1.01x slower                                                       |
| async_generators          | 436 ms                                                 | 455 ms: 1.04x slower                                                       |
| coroutines                | 22.7 ms                                                | 23.9 ms: 1.05x slower                                                      |
| async_tree_io_tg          | 857 ms                                                 | 919 ms: 1.07x slower                                                       |
| async_tree_io             | 842 ms                                                 | 947 ms: 1.13x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.9 ms: 1.13x faster                                                      |
| nbody          | 87.0 ms                                                | 82.2 ms: 1.06x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 218 ms                                                 | 215 ms: 1.02x faster                                                       |
| regex_v8       | 26.2 ms                                                | 25.9 ms: 1.01x faster                                                      |
| regex_effbot   | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                      |
| regex_compile  | 132 ms                                                 | 155 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 191 us: 1.13x faster                                                       |
| xml_etree_process    | 60.6 ms                                                | 54.0 ms: 1.12x faster                                                      |
| xml_etree_generate   | 86.7 ms                                                | 78.1 ms: 1.11x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 144 ms: 1.08x faster                                                       |
| json_dumps           | 10.6 ms                                                | 9.90 ms: 1.07x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 2.06 sec: 1.04x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                                      |
| pickle_pure_python   | 310 us                                                 | 314 us: 1.01x slower                                                       |
| json_loads           | 27.2 us                                                | 29.5 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.8 ms: 1.16x faster                                                      |
| python_startup_no_site | 6.96 ms                                                | 7.19 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.65 ms: 1.15x faster                                                      |
| genshi_text     | 23.5 ms                                                | 22.6 ms: 1.04x faster                                                      |
| django_template | 35.2 ms                                                | 38.8 ms: 1.11x slower                                                      |
| genshi_xml      | 50.9 ms                                                | 59.0 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 27.1 us: 1.44x faster                                                      |
| create_gc_cycles          | 2.41 ms                                                | 1.79 ms: 1.35x faster                                                      |
| deepcopy                  | 358 us                                                 | 267 us: 1.34x faster                                                       |
| scimark_fft               | 364 ms                                                 | 312 ms: 1.17x faster                                                       |
| scimark_monte_carlo       | 67.4 ms                                                | 58.1 ms: 1.16x faster                                                      |
| python_startup            | 12.5 ms                                                | 10.8 ms: 1.16x faster                                                      |
| gc_traversal              | 4.37 ms                                                | 3.78 ms: 1.16x faster                                                      |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.38 ms: 1.15x faster                                                      |
| deepcopy_reduce           | 3.20 us                                                | 2.79 us: 1.15x faster                                                      |
| mako                      | 11.1 ms                                                | 9.65 ms: 1.15x faster                                                      |
| float                     | 79.2 ms                                                | 69.9 ms: 1.13x faster                                                      |
| async_tree_memoization_tg | 464 ms                                                 | 409 ms: 1.13x faster                                                       |
| unpickle_pure_python      | 216 us                                                 | 191 us: 1.13x faster                                                       |
| xml_etree_process         | 60.6 ms                                                | 54.0 ms: 1.12x faster                                                      |
| xml_etree_generate        | 86.7 ms                                                | 78.1 ms: 1.11x faster                                                      |
| pathlib                   | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                      |
| crypto_pyaes              | 75.3 ms                                                | 68.2 ms: 1.10x faster                                                      |
| telco                     | 8.54 ms                                                | 7.75 ms: 1.10x faster                                                      |
| fannkuch                  | 404 ms                                                 | 372 ms: 1.09x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 144 ms: 1.08x faster                                                       |
| spectral_norm             | 115 ms                                                 | 107 ms: 1.07x faster                                                       |
| json_dumps                | 10.6 ms                                                | 9.90 ms: 1.07x faster                                                      |
| nbody                     | 87.0 ms                                                | 82.2 ms: 1.06x faster                                                      |
| bpe_tokeniser             | 4.75 sec                                               | 4.51 sec: 1.05x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 422 ms: 1.05x faster                                                       |
| tomli_loads               | 2.14 sec                                               | 2.06 sec: 1.04x faster                                                     |
| genshi_text               | 23.5 ms                                                | 22.6 ms: 1.04x faster                                                      |
| async_tree_none           | 351 ms                                                 | 339 ms: 1.03x faster                                                       |
| scimark_lu                | 113 ms                                                 | 109 ms: 1.03x faster                                                       |
| xml_etree_iterparse       | 101 ms                                                 | 98.2 ms: 1.03x faster                                                      |
| scimark_sor               | 124 ms                                                 | 122 ms: 1.02x faster                                                       |
| regex_dna                 | 218 ms                                                 | 215 ms: 1.02x faster                                                       |
| json                      | 5.36 ms                                                | 5.29 ms: 1.01x faster                                                      |
| regex_v8                  | 26.2 ms                                                | 25.9 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 571 ms: 1.01x faster                                                       |
| meteor_contest            | 109 ms                                                 | 108 ms: 1.01x faster                                                       |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| mdp                       | 2.72 sec                                               | 2.72 sec: 1.00x faster                                                     |
| asyncio_websockets        | 552 ms                                                 | 557 ms: 1.01x slower                                                       |
| regex_effbot              | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                      |
| pickle_pure_python        | 310 us                                                 | 314 us: 1.01x slower                                                       |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                       |
| coverage                  | 84.0 ms                                                | 85.4 ms: 1.02x slower                                                      |
| deltablue                 | 3.23 ms                                                | 3.29 ms: 1.02x slower                                                      |
| logging_simple            | 5.72 us                                                | 5.88 us: 1.03x slower                                                      |
| comprehensions            | 16.5 us                                                | 17.0 us: 1.03x slower                                                      |
| raytrace                  | 267 ms                                                 | 275 ms: 1.03x slower                                                       |
| python_startup_no_site    | 6.96 ms                                                | 7.19 ms: 1.03x slower                                                      |
| async_generators          | 436 ms                                                 | 455 ms: 1.04x slower                                                       |
| pprint_safe_repr          | 728 ms                                                 | 761 ms: 1.05x slower                                                       |
| coroutines                | 22.7 ms                                                | 23.9 ms: 1.05x slower                                                      |
| nqueens                   | 78.4 ms                                                | 84.0 ms: 1.07x slower                                                      |
| async_tree_io_tg          | 857 ms                                                 | 919 ms: 1.07x slower                                                       |
| chaos                     | 58.1 ms                                                | 62.3 ms: 1.07x slower                                                      |
| json_loads                | 27.2 us                                                | 29.5 us: 1.08x slower                                                      |
| pycparser                 | 1.20 sec                                               | 1.30 sec: 1.09x slower                                                     |
| bench_thread_pool         | 822 us                                                 | 898 us: 1.09x slower                                                       |
| 2to3                      | 267 ms                                                 | 292 ms: 1.09x slower                                                       |
| html5lib                  | 64.2 ms                                                | 70.6 ms: 1.10x slower                                                      |
| richards                  | 48.7 ms                                                | 53.8 ms: 1.10x slower                                                      |
| django_template           | 35.2 ms                                                | 38.8 ms: 1.11x slower                                                      |
| richards_super            | 54.9 ms                                                | 60.8 ms: 1.11x slower                                                      |
| pprint_pformat            | 1.49 sec                                               | 1.66 sec: 1.11x slower                                                     |
| async_tree_io             | 842 ms                                                 | 947 ms: 1.13x slower                                                       |
| genshi_xml                | 50.9 ms                                                | 59.0 ms: 1.16x slower                                                      |
| sqlglot_normalize         | 108 ms                                                 | 125 ms: 1.16x slower                                                       |
| hexiom                    | 6.16 ms                                                | 7.14 ms: 1.16x slower                                                      |
| regex_compile             | 132 ms                                                 | 155 ms: 1.17x slower                                                       |
| sympy_expand              | 463 ms                                                 | 556 ms: 1.20x slower                                                       |
| generators                | 29.0 ms                                                | 34.8 ms: 1.20x slower                                                      |
| go                        | 144 ms                                                 | 178 ms: 1.24x slower                                                       |
| sympy_str                 | 275 ms                                                 | 341 ms: 1.24x slower                                                       |
| sqlglot_optimize          | 53.7 ms                                                | 67.1 ms: 1.25x slower                                                      |
| tornado_http              | 92.4 ms                                                | 119 ms: 1.29x slower                                                       |
| docutils                  | 2.59 sec                                               | 3.47 sec: 1.34x slower                                                     |
| sqlglot_parse             | 1.27 ms                                                | 1.73 ms: 1.36x slower                                                      |
| sqlglot_transpile         | 1.58 ms                                                | 2.17 ms: 1.37x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 27.3 ms: 1.37x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 214 ms: 1.42x slower                                                       |
| pylint                    | 313 ms                                                 | 480 ms: 1.53x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (7): async_tree_none_tg, typing_runtime_protocols, thrift, pyflate, bench_mp_pool, logging_format, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240909-3.14.0a0-f67fedc-JIT/bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.021x slower
# HPT report

- Reliability score: 94.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x
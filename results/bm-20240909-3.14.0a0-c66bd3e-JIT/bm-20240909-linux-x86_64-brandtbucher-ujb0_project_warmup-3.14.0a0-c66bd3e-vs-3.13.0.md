# Results vs. 3.13.0

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: c66bd3e
- commit date: 2024-09-09
- overall geometric mean: 1.013x slower
- HPT reliability: 80.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 292 ms: 1.09x slower                                                       |
| docutils       | 2.59 sec                                               | 3.46 sec: 1.33x slower                                                     |
| html5lib       | 64.2 ms                                                | 73.0 ms: 1.14x slower                                                      |
| tornado_http   | 92.4 ms                                                | 119 ms: 1.28x slower                                                       |
| Geometric mean | (ref)                                                  | 1.21x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 415 ms: 1.12x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 426 ms: 1.04x faster                                                       |
| async_tree_none           | 351 ms                                                 | 338 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 573 ms: 1.01x faster                                                       |
| asyncio_websockets        | 552 ms                                                 | 557 ms: 1.01x slower                                                       |
| async_generators          | 436 ms                                                 | 454 ms: 1.04x slower                                                       |
| async_tree_io_tg          | 857 ms                                                 | 905 ms: 1.06x slower                                                       |
| coroutines                | 22.7 ms                                                | 24.7 ms: 1.09x slower                                                      |
| async_tree_io             | 842 ms                                                 | 951 ms: 1.13x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.8 ms: 1.13x faster                                                      |
| nbody          | 87.0 ms                                                | 83.1 ms: 1.05x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.45 ms: 1.08x faster                                                      |
| regex_dna      | 218 ms                                                 | 206 ms: 1.06x faster                                                       |
| regex_v8       | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                      |
| regex_compile  | 132 ms                                                 | 151 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 53.9 ms: 1.12x faster                                                      |
| xml_etree_generate   | 86.7 ms                                                | 78.8 ms: 1.10x faster                                                      |
| json_dumps           | 10.6 ms                                                | 9.69 ms: 1.09x faster                                                      |
| unpickle_pure_python | 216 us                                                 | 199 us: 1.09x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 97.8 ms: 1.04x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 2.07 sec: 1.03x faster                                                     |
| pickle_pure_python   | 310 us                                                 | 313 us: 1.01x slower                                                       |
| json_loads           | 27.2 us                                                | 29.5 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                      |
| python_startup_no_site | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.78 ms: 1.13x faster                                                      |
| genshi_text     | 23.5 ms                                                | 22.6 ms: 1.04x faster                                                      |
| django_template | 35.2 ms                                                | 40.4 ms: 1.15x slower                                                      |
| genshi_xml      | 50.9 ms                                                | 60.0 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 26.7 us: 1.46x faster                                                      |
| deepcopy                  | 358 us                                                 | 268 us: 1.34x faster                                                       |
| create_gc_cycles          | 2.41 ms                                                | 1.81 ms: 1.33x faster                                                      |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.20 ms: 1.20x faster                                                      |
| deepcopy_reduce           | 3.20 us                                                | 2.69 us: 1.19x faster                                                      |
| richards                  | 48.7 ms                                                | 40.9 ms: 1.19x faster                                                      |
| scimark_fft               | 364 ms                                                 | 307 ms: 1.18x faster                                                       |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                      |
| gc_traversal              | 4.37 ms                                                | 3.76 ms: 1.16x faster                                                      |
| scimark_monte_carlo       | 67.4 ms                                                | 58.4 ms: 1.15x faster                                                      |
| crypto_pyaes              | 75.3 ms                                                | 65.4 ms: 1.15x faster                                                      |
| float                     | 79.2 ms                                                | 69.8 ms: 1.13x faster                                                      |
| mako                      | 11.1 ms                                                | 9.78 ms: 1.13x faster                                                      |
| spectral_norm             | 115 ms                                                 | 102 ms: 1.13x faster                                                       |
| xml_etree_process         | 60.6 ms                                                | 53.9 ms: 1.12x faster                                                      |
| async_tree_memoization_tg | 464 ms                                                 | 415 ms: 1.12x faster                                                       |
| pathlib                   | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                      |
| xml_etree_generate        | 86.7 ms                                                | 78.8 ms: 1.10x faster                                                      |
| json_dumps                | 10.6 ms                                                | 9.69 ms: 1.09x faster                                                      |
| unpickle_pure_python      | 216 us                                                 | 199 us: 1.09x faster                                                       |
| telco                     | 8.54 ms                                                | 7.88 ms: 1.08x faster                                                      |
| fannkuch                  | 404 ms                                                 | 374 ms: 1.08x faster                                                       |
| regex_effbot              | 3.73 ms                                                | 3.45 ms: 1.08x faster                                                      |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.08x faster                                                       |
| mdp                       | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                     |
| richards_super            | 54.9 ms                                                | 51.4 ms: 1.07x faster                                                      |
| pyflate                   | 471 ms                                                 | 441 ms: 1.07x faster                                                       |
| regex_dna                 | 218 ms                                                 | 206 ms: 1.06x faster                                                       |
| nbody                     | 87.0 ms                                                | 83.1 ms: 1.05x faster                                                      |
| bpe_tokeniser             | 4.75 sec                                               | 4.54 sec: 1.04x faster                                                     |
| genshi_text               | 23.5 ms                                                | 22.6 ms: 1.04x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 426 ms: 1.04x faster                                                       |
| async_tree_none           | 351 ms                                                 | 338 ms: 1.04x faster                                                       |
| xml_etree_iterparse       | 101 ms                                                 | 97.8 ms: 1.04x faster                                                      |
| regex_v8                  | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                      |
| scimark_lu                | 113 ms                                                 | 109 ms: 1.03x faster                                                       |
| tomli_loads               | 2.14 sec                                               | 2.07 sec: 1.03x faster                                                     |
| typing_runtime_protocols  | 165 us                                                 | 159 us: 1.03x faster                                                       |
| thrift                    | 809 us                                                 | 795 us: 1.02x faster                                                       |
| json                      | 5.36 ms                                                | 5.29 ms: 1.01x faster                                                      |
| meteor_contest            | 109 ms                                                 | 108 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 573 ms: 1.01x faster                                                       |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| bench_mp_pool             | 24.0 ms                                                | 24.2 ms: 1.01x slower                                                      |
| pickle_pure_python        | 310 us                                                 | 313 us: 1.01x slower                                                       |
| asyncio_websockets        | 552 ms                                                 | 557 ms: 1.01x slower                                                       |
| chaos                     | 58.1 ms                                                | 58.7 ms: 1.01x slower                                                      |
| coverage                  | 84.0 ms                                                | 85.9 ms: 1.02x slower                                                      |
| logging_simple            | 5.72 us                                                | 5.88 us: 1.03x slower                                                      |
| python_startup_no_site    | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                      |
| pprint_safe_repr          | 728 ms                                                 | 753 ms: 1.03x slower                                                       |
| pprint_pformat            | 1.49 sec                                               | 1.56 sec: 1.04x slower                                                     |
| async_generators          | 436 ms                                                 | 454 ms: 1.04x slower                                                       |
| logging_format            | 6.40 us                                                | 6.74 us: 1.05x slower                                                      |
| async_tree_io_tg          | 857 ms                                                 | 905 ms: 1.06x slower                                                       |
| nqueens                   | 78.4 ms                                                | 84.1 ms: 1.07x slower                                                      |
| raytrace                  | 267 ms                                                 | 289 ms: 1.08x slower                                                       |
| json_loads                | 27.2 us                                                | 29.5 us: 1.08x slower                                                      |
| coroutines                | 22.7 ms                                                | 24.7 ms: 1.09x slower                                                      |
| logging_silent            | 102 ns                                                 | 111 ns: 1.09x slower                                                       |
| bench_thread_pool         | 822 us                                                 | 895 us: 1.09x slower                                                       |
| 2to3                      | 267 ms                                                 | 292 ms: 1.09x slower                                                       |
| deltablue                 | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                      |
| pycparser                 | 1.20 sec                                               | 1.34 sec: 1.12x slower                                                     |
| async_tree_io             | 842 ms                                                 | 951 ms: 1.13x slower                                                       |
| html5lib                  | 64.2 ms                                                | 73.0 ms: 1.14x slower                                                      |
| regex_compile             | 132 ms                                                 | 151 ms: 1.14x slower                                                       |
| django_template           | 35.2 ms                                                | 40.4 ms: 1.15x slower                                                      |
| sqlglot_normalize         | 108 ms                                                 | 126 ms: 1.17x slower                                                       |
| genshi_xml                | 50.9 ms                                                | 60.0 ms: 1.18x slower                                                      |
| hexiom                    | 6.16 ms                                                | 7.27 ms: 1.18x slower                                                      |
| generators                | 29.0 ms                                                | 34.3 ms: 1.19x slower                                                      |
| sympy_expand              | 463 ms                                                 | 557 ms: 1.20x slower                                                       |
| go                        | 144 ms                                                 | 178 ms: 1.24x slower                                                       |
| sympy_str                 | 275 ms                                                 | 341 ms: 1.24x slower                                                       |
| sqlglot_optimize          | 53.7 ms                                                | 67.8 ms: 1.26x slower                                                      |
| tornado_http              | 92.4 ms                                                | 119 ms: 1.28x slower                                                       |
| sqlglot_parse             | 1.27 ms                                                | 1.69 ms: 1.33x slower                                                      |
| docutils                  | 2.59 sec                                               | 3.46 sec: 1.33x slower                                                     |
| sqlglot_transpile         | 1.58 ms                                                | 2.15 ms: 1.36x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 27.6 ms: 1.39x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 215 ms: 1.43x slower                                                       |
| pylint                    | 313 ms                                                 | 482 ms: 1.54x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (4): async_tree_none_tg, comprehensions, scimark_sor, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240909-3.14.0a0-c66bd3e-JIT/bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x slower
# HPT report

- Reliability score: 80.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x
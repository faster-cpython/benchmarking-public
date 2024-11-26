# Results vs. 3.13.0

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: 8d668dd
- commit date: 2024-09-10
- overall geometric mean: 1.017x slower
- HPT reliability: 92.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 289 ms: 1.08x slower                                                       |
| docutils       | 2.59 sec                                               | 3.48 sec: 1.34x slower                                                     |
| html5lib       | 64.2 ms                                                | 74.4 ms: 1.16x slower                                                      |
| tornado_http   | 92.4 ms                                                | 114 ms: 1.23x slower                                                       |
| Geometric mean | (ref)                                                  | 1.20x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 411 ms: 1.13x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 423 ms: 1.05x faster                                                       |
| async_tree_none           | 351 ms                                                 | 338 ms: 1.04x faster                                                       |
| async_tree_none_tg        | 321 ms                                                 | 316 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 571 ms: 1.01x faster                                                       |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                       |
| async_generators          | 436 ms                                                 | 457 ms: 1.05x slower                                                       |
| coroutines                | 22.7 ms                                                | 24.1 ms: 1.06x slower                                                      |
| async_tree_io_tg          | 857 ms                                                 | 913 ms: 1.07x slower                                                       |
| async_tree_io             | 842 ms                                                 | 953 ms: 1.13x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 68.4 ms: 1.16x faster                                                      |
| nbody          | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.8 ms: 1.02x faster                                                      |
| regex_effbot   | 3.73 ms                                                | 3.72 ms: 1.00x faster                                                      |
| regex_compile  | 132 ms                                                 | 151 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 54.4 ms: 1.11x faster                                                      |
| xml_etree_generate   | 86.7 ms                                                | 78.7 ms: 1.10x faster                                                      |
| unpickle_pure_python | 216 us                                                 | 196 us: 1.10x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| json_dumps           | 10.6 ms                                                | 9.95 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 98.0 ms: 1.03x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 2.13 sec: 1.01x faster                                                     |
| pickle_pure_python   | 310 us                                                 | 319 us: 1.03x slower                                                       |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.7 ms: 1.17x faster                                                      |
| python_startup_no_site | 6.96 ms                                                | 7.15 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.86 ms: 1.12x faster                                                      |
| genshi_text     | 23.5 ms                                                | 23.1 ms: 1.02x faster                                                      |
| django_template | 35.2 ms                                                | 40.4 ms: 1.15x slower                                                      |
| genshi_xml      | 50.9 ms                                                | 62.3 ms: 1.22x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 27.3 us: 1.43x faster                                                      |
| create_gc_cycles          | 2.41 ms                                                | 1.78 ms: 1.36x faster                                                      |
| deepcopy                  | 358 us                                                 | 280 us: 1.28x faster                                                       |
| gc_traversal              | 4.37 ms                                                | 3.55 ms: 1.23x faster                                                      |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.27 ms: 1.18x faster                                                      |
| scimark_fft               | 364 ms                                                 | 310 ms: 1.18x faster                                                       |
| python_startup            | 12.5 ms                                                | 10.7 ms: 1.17x faster                                                      |
| deepcopy_reduce           | 3.20 us                                                | 2.74 us: 1.17x faster                                                      |
| float                     | 79.2 ms                                                | 68.4 ms: 1.16x faster                                                      |
| scimark_monte_carlo       | 67.4 ms                                                | 58.8 ms: 1.15x faster                                                      |
| async_tree_memoization_tg | 464 ms                                                 | 411 ms: 1.13x faster                                                       |
| mako                      | 11.1 ms                                                | 9.86 ms: 1.12x faster                                                      |
| telco                     | 8.54 ms                                                | 7.62 ms: 1.12x faster                                                      |
| crypto_pyaes              | 75.3 ms                                                | 67.2 ms: 1.12x faster                                                      |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.12x faster                                                       |
| xml_etree_process         | 60.6 ms                                                | 54.4 ms: 1.11x faster                                                      |
| pathlib                   | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                      |
| xml_etree_generate        | 86.7 ms                                                | 78.7 ms: 1.10x faster                                                      |
| unpickle_pure_python      | 216 us                                                 | 196 us: 1.10x faster                                                       |
| nbody                     | 87.0 ms                                                | 79.8 ms: 1.09x faster                                                      |
| pyflate                   | 471 ms                                                 | 436 ms: 1.08x faster                                                       |
| fannkuch                  | 404 ms                                                 | 376 ms: 1.07x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| json_dumps                | 10.6 ms                                                | 9.95 ms: 1.06x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 423 ms: 1.05x faster                                                       |
| bpe_tokeniser             | 4.75 sec                                               | 4.55 sec: 1.04x faster                                                     |
| scimark_sor               | 124 ms                                                 | 119 ms: 1.04x faster                                                       |
| async_tree_none           | 351 ms                                                 | 338 ms: 1.04x faster                                                       |
| xml_etree_iterparse       | 101 ms                                                 | 98.0 ms: 1.03x faster                                                      |
| scimark_lu                | 113 ms                                                 | 110 ms: 1.02x faster                                                       |
| typing_runtime_protocols  | 165 us                                                 | 161 us: 1.02x faster                                                       |
| genshi_text               | 23.5 ms                                                | 23.1 ms: 1.02x faster                                                      |
| json                      | 5.36 ms                                                | 5.25 ms: 1.02x faster                                                      |
| regex_v8                  | 26.2 ms                                                | 25.8 ms: 1.02x faster                                                      |
| async_tree_none_tg        | 321 ms                                                 | 316 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 571 ms: 1.01x faster                                                       |
| richards                  | 48.7 ms                                                | 48.3 ms: 1.01x faster                                                      |
| tomli_loads               | 2.14 sec                                               | 2.13 sec: 1.01x faster                                                     |
| regex_effbot              | 3.73 ms                                                | 3.72 ms: 1.00x faster                                                      |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| mdp                       | 2.72 sec                                               | 2.72 sec: 1.00x faster                                                     |
| meteor_contest            | 109 ms                                                 | 109 ms: 1.00x slower                                                       |
| asyncio_websockets        | 552 ms                                                 | 558 ms: 1.01x slower                                                       |
| comprehensions            | 16.5 us                                                | 16.7 us: 1.02x slower                                                      |
| richards_super            | 54.9 ms                                                | 55.8 ms: 1.02x slower                                                      |
| bench_mp_pool             | 24.0 ms                                                | 24.4 ms: 1.02x slower                                                      |
| logging_simple            | 5.72 us                                                | 5.83 us: 1.02x slower                                                      |
| logging_format            | 6.40 us                                                | 6.53 us: 1.02x slower                                                      |
| pickle_pure_python        | 310 us                                                 | 319 us: 1.03x slower                                                       |
| python_startup_no_site    | 6.96 ms                                                | 7.15 ms: 1.03x slower                                                      |
| chaos                     | 58.1 ms                                                | 59.9 ms: 1.03x slower                                                      |
| coverage                  | 84.0 ms                                                | 86.8 ms: 1.03x slower                                                      |
| async_generators          | 436 ms                                                 | 457 ms: 1.05x slower                                                       |
| raytrace                  | 267 ms                                                 | 281 ms: 1.05x slower                                                       |
| coroutines                | 22.7 ms                                                | 24.1 ms: 1.06x slower                                                      |
| nqueens                   | 78.4 ms                                                | 83.3 ms: 1.06x slower                                                      |
| pprint_safe_repr          | 728 ms                                                 | 776 ms: 1.07x slower                                                       |
| async_tree_io_tg          | 857 ms                                                 | 913 ms: 1.07x slower                                                       |
| 2to3                      | 267 ms                                                 | 289 ms: 1.08x slower                                                       |
| bench_thread_pool         | 822 us                                                 | 892 us: 1.09x slower                                                       |
| json_loads                | 27.2 us                                                | 29.7 us: 1.09x slower                                                      |
| deltablue                 | 3.23 ms                                                | 3.59 ms: 1.11x slower                                                      |
| pprint_pformat            | 1.49 sec                                               | 1.66 sec: 1.11x slower                                                     |
| pycparser                 | 1.20 sec                                               | 1.35 sec: 1.12x slower                                                     |
| async_tree_io             | 842 ms                                                 | 953 ms: 1.13x slower                                                       |
| regex_compile             | 132 ms                                                 | 151 ms: 1.14x slower                                                       |
| django_template           | 35.2 ms                                                | 40.4 ms: 1.15x slower                                                      |
| html5lib                  | 64.2 ms                                                | 74.4 ms: 1.16x slower                                                      |
| sqlglot_normalize         | 108 ms                                                 | 126 ms: 1.18x slower                                                       |
| sqlglot_optimize          | 53.7 ms                                                | 64.0 ms: 1.19x slower                                                      |
| sympy_expand              | 463 ms                                                 | 554 ms: 1.20x slower                                                       |
| generators                | 29.0 ms                                                | 34.7 ms: 1.20x slower                                                      |
| hexiom                    | 6.16 ms                                                | 7.49 ms: 1.22x slower                                                      |
| sympy_str                 | 275 ms                                                 | 336 ms: 1.22x slower                                                       |
| genshi_xml                | 50.9 ms                                                | 62.3 ms: 1.22x slower                                                      |
| go                        | 144 ms                                                 | 176 ms: 1.22x slower                                                       |
| tornado_http              | 92.4 ms                                                | 114 ms: 1.23x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 25.3 ms: 1.27x slower                                                      |
| sqlglot_transpile         | 1.58 ms                                                | 2.08 ms: 1.32x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.68 ms: 1.32x slower                                                      |
| docutils                  | 2.59 sec                                               | 3.48 sec: 1.34x slower                                                     |
| sympy_sum                 | 150 ms                                                 | 209 ms: 1.39x slower                                                       |
| pylint                    | 313 ms                                                 | 454 ms: 1.45x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (4): thrift, regex_dna, logging_silent, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240910-3.14.0a0-8d668dd-JIT/bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.017x slower
# HPT report

- Reliability score: 92.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x
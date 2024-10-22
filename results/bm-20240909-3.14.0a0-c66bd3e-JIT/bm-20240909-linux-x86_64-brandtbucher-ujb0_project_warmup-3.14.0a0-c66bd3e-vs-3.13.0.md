# Results vs. 3.13.0

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: c66bd3e
- commit date: 2024-09-09
- overall geometric mean: 1.04x slower
- HPT reliability: 92.75%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 292 ms: 1.10x slower                                                       |
| docutils       | 2.58 sec                                               | 3.46 sec: 1.34x slower                                                     |
| html5lib       | 64.5 ms                                                | 73.0 ms: 1.13x slower                                                      |
| tornado_http   | 91.5 ms                                                | 119 ms: 1.30x slower                                                       |
| Geometric mean | (ref)                                                  | 1.21x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 415 ms: 1.12x faster                                                       |
| async_tree_none           | 354 ms                                                 | 338 ms: 1.05x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 426 ms: 1.04x faster                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                     |
| async_generators          | 433 ms                                                 | 454 ms: 1.05x slower                                                       |
| asyncio_tcp               | 488 ms                                                 | 520 ms: 1.07x slower                                                       |
| coroutines                | 22.5 ms                                                | 24.7 ms: 1.10x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 905 ms: 1.10x slower                                                       |
| async_tree_io             | 843 ms                                                 | 951 ms: 1.13x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.8 ms: 1.12x faster                                                      |
| nbody          | 85.7 ms                                                | 83.1 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.45 ms: 1.13x faster                                                      |
| regex_dna      | 220 ms                                                 | 206 ms: 1.07x faster                                                       |
| regex_v8       | 25.3 ms                                                | 25.3 ms: 1.00x slower                                                      |
| regex_compile  | 131 ms                                                 | 151 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 53.9 ms: 1.12x faster                                                      |
| xml_etree_generate   | 87.0 ms                                                | 78.8 ms: 1.10x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.08x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 199 us: 1.07x faster                                                       |
| json_dumps           | 10.4 ms                                                | 9.69 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 97.8 ms: 1.04x faster                                                      |
| tomli_loads          | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                     |
| unpickle             | 14.9 us                                                | 14.6 us: 1.02x faster                                                      |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                      |
| pickle_dict          | 33.2 us                                                | 34.3 us: 1.03x slower                                                      |
| pickle_list          | 5.01 us                                                | 5.21 us: 1.04x slower                                                      |
| pickle_pure_python   | 300 us                                                 | 313 us: 1.04x slower                                                       |
| unpickle_list        | 4.96 us                                                | 5.39 us: 1.09x slower                                                      |
| json_loads           | 27.0 us                                                | 29.5 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                      |
| python_startup_no_site | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.78 ms: 1.14x faster                                                      |
| genshi_text     | 22.9 ms                                                | 22.6 ms: 1.01x faster                                                      |
| django_template | 34.4 ms                                                | 40.4 ms: 1.17x slower                                                      |
| genshi_xml      | 50.3 ms                                                | 60.0 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.7 us: 1.42x faster                                                      |
| deepcopy                  | 352 us                                                 | 268 us: 1.32x faster                                                       |
| scimark_fft               | 369 ms                                                 | 307 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.20 ms: 1.20x faster                                                      |
| deepcopy_reduce           | 3.17 us                                                | 2.69 us: 1.18x faster                                                      |
| richards                  | 48.1 ms                                                | 40.9 ms: 1.18x faster                                                      |
| mako                      | 11.1 ms                                                | 9.78 ms: 1.14x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 58.4 ms: 1.13x faster                                                      |
| spectral_norm             | 115 ms                                                 | 102 ms: 1.13x faster                                                       |
| regex_effbot              | 3.88 ms                                                | 3.45 ms: 1.13x faster                                                      |
| float                     | 78.5 ms                                                | 69.8 ms: 1.12x faster                                                      |
| async_tree_memoization_tg | 465 ms                                                 | 415 ms: 1.12x faster                                                       |
| xml_etree_process         | 60.4 ms                                                | 53.9 ms: 1.12x faster                                                      |
| crypto_pyaes              | 73.0 ms                                                | 65.4 ms: 1.12x faster                                                      |
| xml_etree_generate        | 87.0 ms                                                | 78.8 ms: 1.10x faster                                                      |
| pathlib                   | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                      |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.08x faster                                                       |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                     |
| unpickle_pure_python      | 213 us                                                 | 199 us: 1.07x faster                                                       |
| json_dumps                | 10.4 ms                                                | 9.69 ms: 1.07x faster                                                      |
| telco                     | 8.45 ms                                                | 7.88 ms: 1.07x faster                                                      |
| regex_dna                 | 220 ms                                                 | 206 ms: 1.07x faster                                                       |
| richards_super            | 54.4 ms                                                | 51.4 ms: 1.06x faster                                                      |
| scimark_lu                | 115 ms                                                 | 109 ms: 1.06x faster                                                       |
| async_tree_none           | 354 ms                                                 | 338 ms: 1.05x faster                                                       |
| xml_etree_iterparse       | 102 ms                                                 | 97.8 ms: 1.04x faster                                                      |
| pyflate                   | 460 ms                                                 | 441 ms: 1.04x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 426 ms: 1.04x faster                                                       |
| bpe_tokeniser             | 4.69 sec                                               | 4.54 sec: 1.03x faster                                                     |
| nbody                     | 85.7 ms                                                | 83.1 ms: 1.03x faster                                                      |
| sqlite_synth              | 2.85 us                                                | 2.76 us: 1.03x faster                                                      |
| tomli_loads               | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                     |
| fannkuch                  | 381 ms                                                 | 374 ms: 1.02x faster                                                       |
| unpickle                  | 14.9 us                                                | 14.6 us: 1.02x faster                                                      |
| gc_traversal              | 3.81 ms                                                | 3.76 ms: 1.01x faster                                                      |
| genshi_text               | 22.9 ms                                                | 22.6 ms: 1.01x faster                                                      |
| regex_v8                  | 25.3 ms                                                | 25.3 ms: 1.00x slower                                                      |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                      |
| bench_mp_pool             | 24.0 ms                                                | 24.2 ms: 1.01x slower                                                      |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                      |
| pprint_safe_repr          | 744 ms                                                 | 753 ms: 1.01x slower                                                       |
| scimark_sor               | 122 ms                                                 | 124 ms: 1.02x slower                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                     |
| json                      | 5.20 ms                                                | 5.29 ms: 1.02x slower                                                      |
| pickle                    | 11.6 us                                                | 11.8 us: 1.02x slower                                                      |
| coverage                  | 83.7 ms                                                | 85.9 ms: 1.03x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.17 ms: 1.03x slower                                                      |
| pprint_pformat            | 1.51 sec                                               | 1.56 sec: 1.03x slower                                                     |
| pickle_dict               | 33.2 us                                                | 34.3 us: 1.03x slower                                                      |
| logging_simple            | 5.66 us                                                | 5.88 us: 1.04x slower                                                      |
| pickle_list               | 5.01 us                                                | 5.21 us: 1.04x slower                                                      |
| nqueens                   | 80.6 ms                                                | 84.1 ms: 1.04x slower                                                      |
| pickle_pure_python        | 300 us                                                 | 313 us: 1.04x slower                                                       |
| async_generators          | 433 ms                                                 | 454 ms: 1.05x slower                                                       |
| asyncio_tcp               | 488 ms                                                 | 520 ms: 1.07x slower                                                       |
| logging_format            | 6.25 us                                                | 6.74 us: 1.08x slower                                                      |
| unpickle_list             | 4.96 us                                                | 5.39 us: 1.09x slower                                                      |
| logging_silent            | 102 ns                                                 | 111 ns: 1.09x slower                                                       |
| json_loads                | 27.0 us                                                | 29.5 us: 1.09x slower                                                      |
| coroutines                | 22.5 ms                                                | 24.7 ms: 1.10x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 905 ms: 1.10x slower                                                       |
| bench_thread_pool         | 815 us                                                 | 895 us: 1.10x slower                                                       |
| 2to3                      | 265 ms                                                 | 292 ms: 1.10x slower                                                       |
| raytrace                  | 262 ms                                                 | 289 ms: 1.10x slower                                                       |
| pycparser                 | 1.19 sec                                               | 1.34 sec: 1.12x slower                                                     |
| create_gc_cycles          | 1.61 ms                                                | 1.81 ms: 1.13x slower                                                      |
| async_tree_io             | 843 ms                                                 | 951 ms: 1.13x slower                                                       |
| html5lib                  | 64.5 ms                                                | 73.0 ms: 1.13x slower                                                      |
| deltablue                 | 3.15 ms                                                | 3.57 ms: 1.13x slower                                                      |
| regex_compile             | 131 ms                                                 | 151 ms: 1.15x slower                                                       |
| sqlglot_normalize         | 107 ms                                                 | 126 ms: 1.17x slower                                                       |
| django_template           | 34.4 ms                                                | 40.4 ms: 1.17x slower                                                      |
| hexiom                    | 6.13 ms                                                | 7.27 ms: 1.19x slower                                                      |
| generators                | 28.8 ms                                                | 34.3 ms: 1.19x slower                                                      |
| genshi_xml                | 50.3 ms                                                | 60.0 ms: 1.19x slower                                                      |
| sympy_expand              | 462 ms                                                 | 557 ms: 1.21x slower                                                       |
| sympy_str                 | 274 ms                                                 | 341 ms: 1.25x slower                                                       |
| sqlglot_optimize          | 53.9 ms                                                | 67.8 ms: 1.26x slower                                                      |
| go                        | 142 ms                                                 | 178 ms: 1.26x slower                                                       |
| tornado_http              | 91.5 ms                                                | 119 ms: 1.30x slower                                                       |
| sqlglot_parse             | 1.27 ms                                                | 1.69 ms: 1.34x slower                                                      |
| docutils                  | 2.58 sec                                               | 3.46 sec: 1.34x slower                                                     |
| sqlglot_transpile         | 1.57 ms                                                | 2.15 ms: 1.36x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 27.6 ms: 1.39x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 215 ms: 1.44x slower                                                       |
| pylint                    | 313 ms                                                 | 482 ms: 1.54x slower                                                       |
| unpack_sequence           | 42.4 ns                                                | 138 ns: 3.26x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.04x slower                                                               |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, thrift, pidigits, typing_runtime_protocols, meteor_contest, async_tree_none_tg, asyncio_websockets, chaos, async_tree_cpu_io_mixed_tg
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 92.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.20x
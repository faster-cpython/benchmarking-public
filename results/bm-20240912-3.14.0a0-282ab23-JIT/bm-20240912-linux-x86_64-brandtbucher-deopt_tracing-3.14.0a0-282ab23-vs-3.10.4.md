# Results vs. 3.10.4

- fork: brandtbucher
- ref: deopt_tracing
- machine: linux-x86_64
- commit hash: 282ab23
- commit date: 2024-09-12
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                                 |
| docutils       | 3.30 sec                                               | 2.94 sec: 1.12x faster                                               |
| html5lib       | 88.9 ms                                                | 63.3 ms: 1.40x faster                                                |
| tornado_http   | 136 ms                                                 | 94.7 ms: 1.44x faster                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 314 ms: 2.32x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 392 ms: 2.22x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 845 ms: 2.09x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.79x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.09x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.2 ms: 1.91x faster                                                |
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                                |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.49x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.34x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.60x faster                                               |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 54.2 ms: 1.46x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 77.2 ms: 1.29x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                 |
| json_loads           | 31.2 us                                                | 27.3 us: 1.14x faster                                                |
| pickle_list          | 5.08 us                                                | 5.14 us: 1.01x slower                                                |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                                |
| pickle_dict          | 29.6 us                                                | 33.8 us: 1.14x slower                                                |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                         |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.84 ms: 1.66x faster                                                |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                |
| genshi_text     | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                |
| genshi_xml      | 66.0 ms                                                | 59.8 ms: 1.10x faster                                                |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                |
| generators               | 80.1 ms                                                | 33.1 ms: 2.42x faster                                                |
| async_tree_none          | 728 ms                                                 | 314 ms: 2.32x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 392 ms: 2.22x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 26.8 us: 2.18x faster                                                |
| async_tree_io            | 1.77 sec                                               | 845 ms: 2.09x faster                                                 |
| richards_super           | 94.7 ms                                                | 45.7 ms: 2.07x faster                                                |
| richards                 | 79.3 ms                                                | 39.9 ms: 1.99x faster                                                |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                                |
| nbody                    | 154 ms                                                 | 80.2 ms: 1.91x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 67.0 ms: 1.91x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 62.3 ms: 1.90x faster                                                |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 496 ms: 1.86x faster                                                 |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                 |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                 |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                 |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.79x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                                |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                 |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                                |
| mako                     | 16.3 ms                                                | 9.84 ms: 1.66x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.60x faster                                               |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                 |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.87 ms: 1.51x faster                                                |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.36 ms: 1.48x faster                                                |
| pylint                   | 551 ms                                                 | 374 ms: 1.48x faster                                                 |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 54.2 ms: 1.46x faster                                                |
| tornado_http             | 136 ms                                                 | 94.7 ms: 1.44x faster                                                |
| fannkuch                 | 532 ms                                                 | 371 ms: 1.43x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                               |
| html5lib                 | 88.9 ms                                                | 63.3 ms: 1.40x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                               |
| regex_compile            | 188 ms                                                 | 140 ms: 1.34x faster                                                 |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 77.2 ms: 1.29x faster                                                |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                |
| nqueens                  | 106 ms                                                 | 83.5 ms: 1.27x faster                                                |
| genshi_text              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.25x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 67.7 ms: 1.25x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 57.8 ms: 1.20x faster                                                |
| bench_thread_pool        | 986 us                                                 | 835 us: 1.18x faster                                                 |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                                |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                 |
| json_loads               | 31.2 us                                                | 27.3 us: 1.14x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                |
| sympy_expand             | 566 ms                                                 | 500 ms: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                               |
| docutils                 | 3.30 sec                                               | 2.94 sec: 1.12x faster                                               |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                |
| genshi_xml               | 66.0 ms                                                | 59.8 ms: 1.10x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                 |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                 |
| pickle_list              | 5.08 us                                                | 5.14 us: 1.01x slower                                                |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                 |
| coverage                 | 79.4 ms                                                | 83.8 ms: 1.05x slower                                                |
| gc_traversal             | 3.62 ms                                                | 3.83 ms: 1.06x slower                                                |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                                |
| pickle_dict              | 29.6 us                                                | 33.8 us: 1.14x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                |
| unpack_sequence          | 60.0 ns                                                | 108 ns: 1.80x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                         |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-282ab23-JIT/bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.20x
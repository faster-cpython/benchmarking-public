# Results vs. 3.10.4

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 84bca09
- commit date: 2024-07-17
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                                 |
| docutils       | 3.30 sec                                               | 2.88 sec: 1.15x faster                                               |
| html5lib       | 88.9 ms                                                | 63.3 ms: 1.40x faster                                                |
| tornado_http   | 136 ms                                                 | 93.2 ms: 1.46x faster                                                |
| Geometric mean | (ref)                                                  | 1.31x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 407 ms: 2.14x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 846 ms: 2.09x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 564 ms: 1.80x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.5 ms: 1.93x faster                                                |
| float          | 117 ms                                                 | 70.2 ms: 1.67x faster                                                |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.49x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.82 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 293 us: 1.65x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                               |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                 |
| json_loads           | 31.2 us                                                | 27.6 us: 1.13x faster                                                |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.82 ms: 1.66x faster                                                |
| django_template | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                |
| genshi_text     | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                |
| genshi_xml      | 66.0 ms                                                | 53.4 ms: 1.24x faster                                                |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                                 |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.65 ms: 2.17x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 407 ms: 2.14x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 846 ms: 2.09x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 28.7 us: 2.03x faster                                                |
| richards_super           | 94.7 ms                                                | 47.2 ms: 2.01x faster                                                |
| chaos                    | 115 ms                                                 | 57.5 ms: 2.01x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 60.9 ms: 1.94x faster                                                |
| nbody                    | 154 ms                                                 | 79.5 ms: 1.93x faster                                                |
| richards                 | 79.3 ms                                                | 41.3 ms: 1.92x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 67.9 ms: 1.88x faster                                                |
| raytrace                 | 507 ms                                                 | 272 ms: 1.87x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 564 ms: 1.80x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.78x faster                                                |
| generators               | 80.1 ms                                                | 45.4 ms: 1.76x faster                                                |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                 |
| deepcopy                 | 479 us                                                 | 276 us: 1.74x faster                                                 |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                 |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.69x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                |
| float                    | 117 ms                                                 | 70.2 ms: 1.67x faster                                                |
| mako                     | 16.3 ms                                                | 9.82 ms: 1.66x faster                                                |
| pickle_pure_python       | 484 us                                                 | 293 us: 1.65x faster                                                 |
| go                       | 240 ms                                                 | 145 ms: 1.65x faster                                                 |
| pyflate                  | 716 ms                                                 | 434 ms: 1.65x faster                                                 |
| pylint                   | 551 ms                                                 | 338 ms: 1.63x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                               |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.68 ms: 1.56x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.51x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.35 ms: 1.49x faster                                                |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                                |
| fannkuch                 | 532 ms                                                 | 360 ms: 1.48x faster                                                 |
| tornado_http             | 136 ms                                                 | 93.2 ms: 1.46x faster                                                |
| scimark_lu               | 176 ms                                                 | 122 ms: 1.44x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                               |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 720 ms: 1.41x faster                                                 |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                 |
| html5lib                 | 88.9 ms                                                | 63.3 ms: 1.40x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                |
| thrift                   | 1.07 ms                                                | 793 us: 1.35x faster                                                 |
| django_template          | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                |
| genshi_text              | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                               |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 55.4 ms: 1.25x faster                                                |
| genshi_xml               | 66.0 ms                                                | 53.4 ms: 1.24x faster                                                |
| nqueens                  | 106 ms                                                 | 85.6 ms: 1.24x faster                                                |
| dulwich_log              | 84.3 ms                                                | 68.3 ms: 1.23x faster                                                |
| dask                     | 441 ms                                                 | 361 ms: 1.22x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 828 us: 1.19x faster                                                 |
| sympy_sum                | 196 ms                                                 | 165 ms: 1.19x faster                                                 |
| sympy_str                | 346 ms                                                 | 295 ms: 1.17x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.88 sec: 1.15x faster                                               |
| sympy_expand             | 566 ms                                                 | 496 ms: 1.14x faster                                                 |
| json_loads               | 31.2 us                                                | 27.6 us: 1.13x faster                                                |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                 |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                               |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                 |
| gc_traversal             | 3.62 ms                                                | 3.66 ms: 1.01x slower                                                |
| async_generators         | 444 ms                                                 | 450 ms: 1.01x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.82 ms: 1.05x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                |
| telco                    | 7.27 ms                                                | 8.03 ms: 1.10x slower                                                |
| coverage                 | 79.4 ms                                                | 93.6 ms: 1.18x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                         |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_dna
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240717-3.14.0a0-84bca09-JIT/bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x
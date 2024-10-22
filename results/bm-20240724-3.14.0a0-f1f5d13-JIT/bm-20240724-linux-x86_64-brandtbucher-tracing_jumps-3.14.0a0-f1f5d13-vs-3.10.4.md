# Results vs. 3.10.4

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: f1f5d13
- commit date: 2024-07-24
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                 |
| docutils       | 3.30 sec                                               | 2.90 sec: 1.14x faster                                               |
| html5lib       | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                |
| tornado_http   | 136 ms                                                 | 93.7 ms: 1.46x faster                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 402 ms: 2.16x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 899 ms: 1.97x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.80x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.2 ms: 1.91x faster                                                |
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.48x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                 |
| regex_v8       | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                |
| regex_dna      | 227 ms                                                 | 237 ms: 1.04x slower                                                 |
| regex_effbot   | 3.63 ms                                                | 3.97 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 294 us: 1.65x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                               |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.38x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 79.3 ms: 1.25x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                 |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                                |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.68 ms: 1.69x faster                                                |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                |
| genshi_xml      | 66.0 ms                                                | 53.2 ms: 1.24x faster                                                |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                 |
| generators               | 80.1 ms                                                | 32.8 ms: 2.44x faster                                                |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.56 ms: 2.22x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 402 ms: 2.16x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.05x faster                                                |
| richards_super           | 94.7 ms                                                | 46.8 ms: 2.02x faster                                                |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                                |
| async_tree_io            | 1.77 sec                                               | 899 ms: 1.97x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 60.1 ms: 1.97x faster                                                |
| richards                 | 79.3 ms                                                | 40.5 ms: 1.96x faster                                                |
| nbody                    | 154 ms                                                 | 80.2 ms: 1.91x faster                                                |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 67.4 ms: 1.90x faster                                                |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.80x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.1 us: 1.78x faster                                                |
| deepcopy                 | 479 us                                                 | 273 us: 1.75x faster                                                 |
| scimark_sor              | 220 ms                                                 | 130 ms: 1.69x faster                                                 |
| pyflate                  | 716 ms                                                 | 424 ms: 1.69x faster                                                 |
| mako                     | 16.3 ms                                                | 9.68 ms: 1.69x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                |
| pickle_pure_python       | 484 us                                                 | 294 us: 1.65x faster                                                 |
| go                       | 240 ms                                                 | 146 ms: 1.65x faster                                                 |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                               |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                |
| pylint                   | 551 ms                                                 | 354 ms: 1.56x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.74 ms: 1.54x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                 |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.44 ms: 1.46x faster                                                |
| tornado_http             | 136 ms                                                 | 93.7 ms: 1.46x faster                                                |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                               |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.42x faster                                                 |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.38x faster                                                |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                |
| thrift                   | 1.07 ms                                                | 790 us: 1.36x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                               |
| html5lib                 | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                |
| nqueens                  | 106 ms                                                 | 83.6 ms: 1.27x faster                                                |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 79.3 ms: 1.25x faster                                                |
| genshi_xml               | 66.0 ms                                                | 53.2 ms: 1.24x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 55.8 ms: 1.24x faster                                                |
| dask                     | 441 ms                                                 | 362 ms: 1.22x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 818 us: 1.21x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 69.9 ms: 1.21x faster                                                |
| sympy_str                | 346 ms                                                 | 297 ms: 1.17x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                                |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.16x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                 |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.90 sec: 1.14x faster                                               |
| sympy_expand             | 566 ms                                                 | 504 ms: 1.12x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                               |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                                |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                                |
| regex_v8                 | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                 |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                 |
| regex_dna                | 227 ms                                                 | 237 ms: 1.04x slower                                                 |
| telco                    | 7.27 ms                                                | 7.84 ms: 1.08x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                |
| regex_effbot             | 3.63 ms                                                | 3.97 ms: 1.09x slower                                                |
| coverage                 | 79.4 ms                                                | 91.5 ms: 1.15x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                         |

Benchmark hidden because not significant (2): bench_mp_pool, gc_traversal
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240724-3.14.0a0-f1f5d13-JIT/bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.21x
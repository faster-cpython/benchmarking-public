# Results vs. 3.10.4

- fork: brandtbucher
- ref: dynamic_exit
- machine: linux-x86_64
- commit hash: a8158ae
- commit date: 2024-05-05
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 284 ms: 1.23x faster                                                 |
| chameleon      | 9.68 ms                                                | 7.30 ms: 1.33x faster                                                |
| html5lib       | 88.9 ms                                                | 70.5 ms: 1.26x faster                                                |
| tornado_http   | 136 ms                                                 | 98.0 ms: 1.39x faster                                                |
| Geometric mean | (ref)                                                  | 1.30x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 371 ms: 1.96x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 927 ms: 1.91x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 469 ms: 1.85x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 625 ms: 1.63x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.83x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.0 ms: 1.94x faster                                                |
| float          | 117 ms                                                 | 72.3 ms: 1.62x faster                                                |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.47x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.34x faster                                                 |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.60x faster                                               |
| unpickle_pure_python | 331 us                                                 | 224 us: 1.47x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                 |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 153 ms: 1.10x faster                                                 |
| pickle_list          | 5.08 us                                                | 4.99 us: 1.02x faster                                                |
| unpickle_list        | 5.20 us                                                | 5.39 us: 1.04x slower                                                |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                                |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                |
| pickle_dict          | 29.6 us                                                | 35.5 us: 1.20x slower                                                |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.66 ms: 1.29x slower                                                |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.67 ms: 1.69x faster                                                |
| django_template | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                |
| genshi_xml      | 66.0 ms                                                | 58.2 ms: 1.13x faster                                                |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 175 us: 3.10x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.86 ms: 2.05x faster                                                |
| chaos                    | 115 ms                                                 | 58.2 ms: 1.98x faster                                                |
| async_tree_none          | 728 ms                                                 | 371 ms: 1.96x faster                                                 |
| nbody                    | 154 ms                                                 | 79.0 ms: 1.94x faster                                                |
| richards_super           | 94.7 ms                                                | 49.3 ms: 1.92x faster                                                |
| async_tree_io            | 1.77 sec                                               | 927 ms: 1.91x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 469 ms: 1.85x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 69.1 ms: 1.85x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 64.2 ms: 1.84x faster                                                |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.84x faster                                                |
| raytrace                 | 507 ms                                                 | 282 ms: 1.80x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 521 ms: 1.77x faster                                                 |
| logging_silent           | 190 ns                                                 | 109 ns: 1.74x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                |
| spectral_norm            | 170 ms                                                 | 99.0 ms: 1.72x faster                                                |
| mako                     | 16.3 ms                                                | 9.67 ms: 1.69x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                |
| scimark_sor              | 220 ms                                                 | 133 ms: 1.65x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 625 ms: 1.63x faster                                                 |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                 |
| float                    | 117 ms                                                 | 72.3 ms: 1.62x faster                                                |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.60x faster                                               |
| pyflate                  | 716 ms                                                 | 452 ms: 1.59x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.60 ms: 1.58x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                |
| generators               | 80.1 ms                                                | 51.4 ms: 1.56x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 37.8 us: 1.55x faster                                                |
| pylint                   | 551 ms                                                 | 364 ms: 1.52x faster                                                 |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                |
| fannkuch                 | 532 ms                                                 | 359 ms: 1.48x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 224 us: 1.47x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.75 us: 1.44x faster                                                |
| logging_format           | 9.09 us                                                | 6.43 us: 1.41x faster                                                |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 731 ms: 1.39x faster                                                 |
| tornado_http             | 136 ms                                                 | 98.0 ms: 1.39x faster                                                |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                               |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                               |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                |
| regex_compile            | 188 ms                                                 | 141 ms: 1.34x faster                                                 |
| chameleon                | 9.68 ms                                                | 7.30 ms: 1.33x faster                                                |
| thrift                   | 1.07 ms                                                | 810 us: 1.32x faster                                                 |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                |
| deepcopy                 | 479 us                                                 | 368 us: 1.30x faster                                                 |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 3.30 us: 1.26x faster                                                |
| html5lib                 | 88.9 ms                                                | 70.5 ms: 1.26x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.23x faster                                                 |
| 2to3                     | 348 ms                                                 | 284 ms: 1.23x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 57.0 ms: 1.21x faster                                                |
| dulwich_log              | 84.3 ms                                                | 70.4 ms: 1.20x faster                                                |
| nqueens                  | 106 ms                                                 | 88.4 ms: 1.20x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                                |
| djangocms                | 38.4 us                                                | 32.6 us: 1.18x faster                                                |
| dask                     | 441 ms                                                 | 378 ms: 1.17x faster                                                 |
| sympy_str                | 346 ms                                                 | 302 ms: 1.15x faster                                                 |
| aiohttp                  | 1.44 ms                                                | 1.26 ms: 1.14x faster                                                |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                 |
| pathlib                  | 20.5 ms                                                | 17.9 ms: 1.14x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 58.2 ms: 1.13x faster                                                |
| gunicorn                 | 1.53 ms                                                | 1.35 ms: 1.13x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 153 ms: 1.10x faster                                                 |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                 |
| json                     | 5.69 ms                                                | 5.20 ms: 1.09x faster                                                |
| mypy2                    | 894 ms                                                 | 822 ms: 1.09x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.06x faster                                                |
| pickle_list              | 5.08 us                                                | 4.99 us: 1.02x faster                                                |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                 |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                |
| unpickle_list            | 5.20 us                                                | 5.39 us: 1.04x slower                                                |
| async_generators         | 444 ms                                                 | 465 ms: 1.05x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                                |
| flaskblogging            | 8.58 ms                                                | 9.25 ms: 1.08x slower                                                |
| coverage                 | 79.4 ms                                                | 87.1 ms: 1.10x slower                                                |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.12 ms: 1.14x slower                                                |
| telco                    | 7.27 ms                                                | 8.37 ms: 1.15x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.87 ms: 1.16x slower                                                |
| pickle_dict              | 29.6 us                                                | 35.5 us: 1.20x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.66 ms: 1.29x slower                                                |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                         |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240505-3.13.0a6+-a8158ae-JIT/bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.21x
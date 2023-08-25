
# Results vs. 3.10.4

- fork: itamaro
- ref: eager_tasks_factory
- machine: linux-x86_64
- commit hash: bcf40dc
- commit date: 2023-03-20
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.27 ms: 1.44x faster                                                  |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.6 ms: 1.62x faster                                                  |
| float          | 111 ms                                                 | 74.0 ms: 1.49x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                  |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.30 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 281 us: 1.62x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.51 ms: 1.42x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 55.3 ms: 1.36x faster                                                  |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.1 ms: 1.18x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.21 us: 1.08x faster                                                  |
| unpickle             | 14.1 us                                                | 13.4 us: 1.05x faster                                                  |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.55 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                  |
| genshi_text     | 30.3 ms                                                | 21.0 ms: 1.44x faster                                                  |
| django_template | 45.9 ms                                                | 33.2 ms: 1.38x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 47.8 ms: 1.32x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6+-bcf40dc |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.4 ms: 2.61x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.14 ms: 2.36x faster                                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                   |
| asyncio_tcp             | 925 ms                                                 | 506 ms: 1.83x faster                                                   |
| logging_silent          | 175 ns                                                 | 96.2 ns: 1.82x faster                                                  |
| richards                | 74.9 ms                                                | 42.0 ms: 1.78x faster                                                  |
| spectral_norm           | 150 ms                                                 | 88.2 ms: 1.70x faster                                                  |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                   |
| pyflate                 | 673 ms                                                 | 403 ms: 1.67x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 65.5 ms: 1.65x faster                                                  |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                   |
| chaos                   | 106 ms                                                 | 65.5 ms: 1.62x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 281 us: 1.62x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 73.2 ms: 1.62x faster                                                  |
| nbody                   | 142 ms                                                 | 87.6 ms: 1.62x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.08 ms: 1.57x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 34.0 us: 1.54x faster                                                  |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                   |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                                   |
| unpack_sequence         | 64.7 ns                                                | 42.9 ns: 1.51x faster                                                  |
| float                   | 111 ms                                                 | 74.0 ms: 1.49x faster                                                  |
| mako                    | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.27 ms: 1.44x faster                                                  |
| genshi_text             | 30.3 ms                                                | 21.0 ms: 1.44x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                  |
| logging_format          | 8.91 us                                                | 6.23 us: 1.43x faster                                                  |
| scimark_fft             | 424 ms                                                 | 297 ms: 1.42x faster                                                   |
| json_dumps              | 13.5 ms                                                | 9.51 ms: 1.42x faster                                                  |
| coroutines              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.69 us: 1.42x faster                                                  |
| html5lib                | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.41x faster                                                 |
| pprint_safe_repr        | 955 ms                                                 | 687 ms: 1.39x faster                                                   |
| django_template         | 45.9 ms                                                | 33.2 ms: 1.38x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 619 ms: 1.38x faster                                                   |
| async_tree_none         | 717 ms                                                 | 521 ms: 1.38x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.38x faster                                                 |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                  |
| deepcopy                | 442 us                                                 | 323 us: 1.37x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 55.3 ms: 1.36x faster                                                  |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                  |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                                 |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                   |
| fannkuch                | 486 ms                                                 | 365 ms: 1.33x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 47.8 ms: 1.32x faster                                                  |
| thrift                  | 1.03 ms                                                | 788 us: 1.31x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.31x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.18 ms: 1.30x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 736 ms: 1.29x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                                  |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                                   |
| nqueens                 | 100 ms                                                 | 78.2 ms: 1.28x faster                                                  |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                 |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                   |
| bench_thread_pool       | 947 us                                                 | 783 us: 1.21x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.20x faster                                                  |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                                  |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                   |
| json                    | 5.42 ms                                                | 4.59 ms: 1.18x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.1 ms: 1.18x faster                                                  |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                                   |
| comprehensions          | 26.8 us                                                | 23.4 us: 1.15x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                  |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                  |
| djangocms               | 35.9 us                                                | 32.2 us: 1.12x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.10x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.21 us: 1.08x faster                                                  |
| unpickle                | 14.1 us                                                | 13.4 us: 1.05x faster                                                  |
| async_generators        | 425 ms                                                 | 411 ms: 1.03x faster                                                   |
| telco                   | 6.54 ms                                                | 6.36 ms: 1.03x faster                                                  |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.30 ms: 1.02x slower                                                  |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                                  |
| gc_traversal            | 3.84 ms                                                | 3.98 ms: 1.04x slower                                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.55 ms: 1.13x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.3 us: 1.15x slower                                                  |
| dask                    | 423 ms                                                 | 499 ms: 1.18x slower                                                   |
| coverage                | 72.8 ms                                                | 96.8 ms: 1.33x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

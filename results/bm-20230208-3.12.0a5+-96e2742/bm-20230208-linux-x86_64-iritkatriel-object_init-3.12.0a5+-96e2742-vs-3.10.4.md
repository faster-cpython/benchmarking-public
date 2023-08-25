
# Results vs. 3.10.4

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 96e2742
- commit date: 2023-02-08
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                               |
| chameleon      | 9.06 ms                                                | 6.48 ms: 1.40x faster                                              |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                             |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                              |
| tornado_http   | 127 ms                                                 | 94.1 ms: 1.35x faster                                              |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 86.6 ms: 1.63x faster                                              |
| float          | 111 ms                                                 | 71.8 ms: 1.54x faster                                              |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                               |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                              |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                               |
| regex_effbot   | 3.23 ms                                                | 3.40 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 289 us: 1.58x faster                                               |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                               |
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                              |
| xml_etree_process    | 74.9 ms                                                | 55.4 ms: 1.35x faster                                              |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 80.0 ms: 1.18x faster                                              |
| pickle_list          | 4.56 us                                                | 4.03 us: 1.13x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                               |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                               |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                              |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                              |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                              |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.90 ms: 1.59x faster                                              |
| python_startup_no_site | 5.82 ms                                                | 6.45 ms: 1.11x slower                                              |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.64 ms: 1.53x faster                                              |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                              |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                              |
| genshi_xml      | 63.3 ms                                                | 46.3 ms: 1.37x faster                                              |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.32x faster                                              |
| asyncio_tcp             | 925 ms                                                 | 493 ms: 1.88x faster                                               |
| logging_silent          | 175 ns                                                 | 93.6 ns: 1.87x faster                                              |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                               |
| richards                | 74.9 ms                                                | 42.6 ms: 1.76x faster                                              |
| go                      | 229 ms                                                 | 135 ms: 1.69x faster                                               |
| pyflate                 | 673 ms                                                 | 403 ms: 1.67x faster                                               |
| chaos                   | 106 ms                                                 | 64.3 ms: 1.65x faster                                              |
| raytrace                | 464 ms                                                 | 282 ms: 1.65x faster                                               |
| scimark_monte_carlo     | 108 ms                                                 | 65.8 ms: 1.65x faster                                              |
| nbody                   | 142 ms                                                 | 86.6 ms: 1.63x faster                                              |
| crypto_pyaes            | 118 ms                                                 | 73.0 ms: 1.62x faster                                              |
| python_startup          | 14.2 ms                                                | 8.90 ms: 1.59x faster                                              |
| spectral_norm           | 150 ms                                                 | 94.3 ms: 1.59x faster                                              |
| hexiom                  | 9.53 ms                                                | 6.00 ms: 1.59x faster                                              |
| pickle_pure_python      | 455 us                                                 | 289 us: 1.58x faster                                               |
| float                   | 111 ms                                                 | 71.8 ms: 1.54x faster                                              |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                               |
| mako                    | 14.8 ms                                                | 9.64 ms: 1.53x faster                                              |
| deepcopy_memo           | 52.3 us                                                | 34.3 us: 1.52x faster                                              |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                               |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                              |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.45x faster                                              |
| unpack_sequence         | 64.7 ns                                                | 44.6 ns: 1.45x faster                                              |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                              |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.43x faster                                              |
| logging_format          | 8.91 us                                                | 6.27 us: 1.42x faster                                              |
| scimark_fft             | 424 ms                                                 | 298 ms: 1.42x faster                                               |
| pprint_safe_repr        | 955 ms                                                 | 674 ms: 1.42x faster                                               |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                              |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                              |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.41x faster                                              |
| chameleon               | 9.06 ms                                                | 6.48 ms: 1.40x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.91 ms: 1.39x faster                                              |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                               |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                              |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                               |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                             |
| thrift                  | 1.03 ms                                                | 756 us: 1.37x faster                                               |
| genshi_xml              | 63.3 ms                                                | 46.3 ms: 1.37x faster                                              |
| tornado_http            | 127 ms                                                 | 94.1 ms: 1.35x faster                                              |
| xml_etree_process       | 74.9 ms                                                | 55.4 ms: 1.35x faster                                              |
| deepcopy                | 442 us                                                 | 327 us: 1.35x faster                                               |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                             |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                              |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                               |
| deepcopy_reduce         | 3.82 us                                                | 2.89 us: 1.32x faster                                              |
| async_tree_memoization  | 854 ms                                                 | 652 ms: 1.31x faster                                               |
| mypy2                   | 428 ms                                                 | 329 ms: 1.30x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                              |
| fannkuch                | 486 ms                                                 | 382 ms: 1.27x faster                                               |
| nqueens                 | 100 ms                                                 | 78.9 ms: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 951 ms                                                 | 751 ms: 1.27x faster                                               |
| coroutines              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                              |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                             |
| sympy_integrate         | 24.3 ms                                                | 19.9 ms: 1.22x faster                                              |
| sympy_str               | 328 ms                                                 | 271 ms: 1.21x faster                                               |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                              |
| bench_thread_pool       | 947 us                                                 | 784 us: 1.21x faster                                               |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                              |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                               |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                               |
| json                    | 5.42 ms                                                | 4.56 ms: 1.19x faster                                              |
| xml_etree_generate      | 94.2 ms                                                | 80.0 ms: 1.18x faster                                              |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.1 ms: 1.17x faster                                              |
| sympy_sum               | 185 ms                                                 | 158 ms: 1.17x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.45 ms: 1.15x faster                                              |
| sqlite_synth            | 2.93 us                                                | 2.55 us: 1.15x faster                                              |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                              |
| pickle_list             | 4.56 us                                                | 4.03 us: 1.13x faster                                              |
| djangocms               | 35.9 us                                                | 32.7 us: 1.10x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                               |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                              |
| meteor_contest          | 115 ms                                                 | 108 ms: 1.06x faster                                               |
| mdp                     | 2.82 sec                                               | 2.66 sec: 1.06x faster                                             |
| gc_traversal            | 3.84 ms                                                | 3.65 ms: 1.05x faster                                              |
| regex_dna               | 222 ms                                                 | 211 ms: 1.05x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                               |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                              |
| telco                   | 6.54 ms                                                | 6.47 ms: 1.01x faster                                              |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                               |
| async_generators        | 425 ms                                                 | 431 ms: 1.01x slower                                               |
| generators              | 76.8 ms                                                | 78.2 ms: 1.02x slower                                              |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                              |
| regex_effbot            | 3.23 ms                                                | 3.40 ms: 1.05x slower                                              |
| python_startup_no_site  | 5.82 ms                                                | 6.45 ms: 1.11x slower                                              |
| pickle_dict             | 27.3 us                                                | 31.0 us: 1.14x slower                                              |
| coverage                | 72.8 ms                                                | 96.9 ms: 1.33x slower                                              |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                       |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

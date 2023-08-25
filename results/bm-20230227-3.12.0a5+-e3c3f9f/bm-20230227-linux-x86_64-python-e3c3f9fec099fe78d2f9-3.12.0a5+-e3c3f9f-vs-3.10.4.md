
# Results vs. 3.10.4

- fork: python
- ref: e3c3f9fec099fe78d2f9
- machine: linux-x86_64
- commit hash: e3c3f9f
- commit date: 2023-02-27
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 247 ms: 1.36x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.37 ms: 1.42x faster                                                  |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                 |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                  |
| tornado_http   | 127 ms                                                 | 94.2 ms: 1.35x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.5 ms: 1.53x faster                                                  |
| nbody          | 142 ms                                                 | 96.0 ms: 1.48x faster                                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                  |
| regex_dna      | 222 ms                                                 | 198 ms: 1.12x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 280 us: 1.63x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 195 us: 1.54x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.52 ms: 1.42x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 55.1 ms: 1.36x faster                                                  |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 99.8 ms: 1.12x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                   |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.33 us: 1.05x faster                                                  |
| unpickle_list        | 4.82 us                                                | 5.08 us: 1.05x slower                                                  |
| pickle_dict          | 27.3 us                                                | 32.5 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.95 ms: 1.58x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                  |
| genshi_text     | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                  |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.9 ms: 2.56x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.11 ms: 2.39x faster                                                  |
| logging_silent          | 175 ns                                                 | 92.2 ns: 1.90x faster                                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.88x faster                                                   |
| asyncio_tcp             | 925 ms                                                 | 503 ms: 1.84x faster                                                   |
| richards                | 74.9 ms                                                | 41.0 ms: 1.83x faster                                                  |
| go                      | 229 ms                                                 | 132 ms: 1.73x faster                                                   |
| pyflate                 | 673 ms                                                 | 405 ms: 1.66x faster                                                   |
| raytrace                | 464 ms                                                 | 280 ms: 1.66x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 72.1 ms: 1.64x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 280 us: 1.63x faster                                                   |
| spectral_norm           | 150 ms                                                 | 94.0 ms: 1.60x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.00 ms: 1.59x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 68.3 ms: 1.58x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.95 ms: 1.58x faster                                                  |
| chaos                   | 106 ms                                                 | 68.2 ms: 1.56x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 195 us: 1.54x faster                                                   |
| unpack_sequence         | 64.7 ns                                                | 42.2 ns: 1.53x faster                                                  |
| float                   | 111 ms                                                 | 72.5 ms: 1.53x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 34.6 us: 1.51x faster                                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                   |
| mako                    | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                  |
| nbody                   | 142 ms                                                 | 96.0 ms: 1.48x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.45x faster                                                  |
| genshi_text             | 30.3 ms                                                | 20.9 ms: 1.45x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                 |
| chameleon               | 9.06 ms                                                | 6.37 ms: 1.42x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.52 ms: 1.42x faster                                                  |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 680 ms: 1.40x faster                                                   |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                  |
| logging_format          | 8.91 us                                                | 6.38 us: 1.40x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.79 us: 1.39x faster                                                  |
| fannkuch                | 486 ms                                                 | 352 ms: 1.38x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.38x faster                                                 |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                  |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                 |
| xml_etree_process       | 74.9 ms                                                | 55.1 ms: 1.36x faster                                                  |
| 2to3                    | 336 ms                                                 | 247 ms: 1.36x faster                                                   |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                                   |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.36x faster                                                  |
| scimark_fft             | 424 ms                                                 | 313 ms: 1.35x faster                                                   |
| tornado_http            | 127 ms                                                 | 94.2 ms: 1.35x faster                                                  |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                  |
| coroutines              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                  |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 649 ms: 1.32x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                   |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 743 ms: 1.28x faster                                                   |
| nqueens                 | 100 ms                                                 | 78.4 ms: 1.28x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 3.02 us: 1.26x faster                                                  |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.48 ms: 1.22x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                   |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 786 us: 1.21x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 63.3 ms: 1.20x faster                                                  |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                   |
| json                    | 5.42 ms                                                | 4.53 ms: 1.20x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.18x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                                  |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                                   |
| xml_etree_generate      | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                  |
| djangocms               | 35.9 us                                                | 31.9 us: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                                  |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                   |
| regex_dna               | 222 ms                                                 | 198 ms: 1.12x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 99.8 ms: 1.12x faster                                                  |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.64 us: 1.11x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                   |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| pickle_list             | 4.56 us                                                | 4.33 us: 1.05x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.69 sec: 1.05x faster                                                 |
| async_generators        | 425 ms                                                 | 409 ms: 1.04x faster                                                   |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                   |
| unpickle_list           | 4.82 us                                                | 5.08 us: 1.05x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                  |
| gc_traversal            | 3.84 ms                                                | 4.30 ms: 1.12x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                  |
| dask                    | 423 ms                                                 | 498 ms: 1.18x slower                                                   |
| pickle_dict             | 27.3 us                                                | 32.5 us: 1.19x slower                                                  |
| coverage                | 72.8 ms                                                | 96.5 ms: 1.33x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (3): telco, bench_mp_pool, pickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

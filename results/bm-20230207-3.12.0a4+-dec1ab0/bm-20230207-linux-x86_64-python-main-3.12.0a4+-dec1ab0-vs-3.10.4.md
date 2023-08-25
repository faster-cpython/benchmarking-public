
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: dec1ab0
- commit date: 2023-02-07
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 254 ms: 1.32x faster                                   |
| chameleon      | 9.06 ms                                                | 6.27 ms: 1.45x faster                                  |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                 |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                  |
| tornado_http   | 127 ms                                                 | 94.6 ms: 1.35x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.1 ms: 1.53x faster                                  |
| nbody          | 142 ms                                                 | 95.4 ms: 1.48x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.44 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                   |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.53x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.41 ms: 1.44x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.9 ms: 1.39x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 77.3 ms: 1.22x faster                                  |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| pickle_list          | 4.56 us                                                | 4.16 us: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle             | 14.1 us                                                | 13.0 us: 1.08x faster                                  |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                  |
| unpickle_list        | 4.82 us                                                | 5.04 us: 1.05x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.2 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.97 ms: 1.58x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.72 ms: 1.52x faster                                  |
| genshi_text     | 30.3 ms                                                | 20.4 ms: 1.49x faster                                  |
| django_template | 45.9 ms                                                | 33.5 ms: 1.37x faster                                  |
| genshi_xml      | 63.3 ms                                                | 46.7 ms: 1.36x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.30 ms: 2.25x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 494 ms: 1.87x faster                                   |
| logging_silent          | 175 ns                                                 | 93.8 ns: 1.87x faster                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                   |
| richards                | 74.9 ms                                                | 41.8 ms: 1.79x faster                                  |
| pyflate                 | 673 ms                                                 | 399 ms: 1.68x faster                                   |
| go                      | 229 ms                                                 | 138 ms: 1.67x faster                                   |
| chaos                   | 106 ms                                                 | 65.5 ms: 1.62x faster                                  |
| raytrace                | 464 ms                                                 | 287 ms: 1.62x faster                                   |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 74.4 ms: 1.59x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 68.1 ms: 1.59x faster                                  |
| hexiom                  | 9.53 ms                                                | 5.99 ms: 1.59x faster                                  |
| python_startup          | 14.2 ms                                                | 8.97 ms: 1.58x faster                                  |
| spectral_norm           | 150 ms                                                 | 96.5 ms: 1.55x faster                                  |
| float                   | 111 ms                                                 | 72.1 ms: 1.53x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.53x faster                                   |
| mako                    | 14.8 ms                                                | 9.72 ms: 1.52x faster                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                   |
| genshi_text             | 30.3 ms                                                | 20.4 ms: 1.49x faster                                  |
| nbody                   | 142 ms                                                 | 95.4 ms: 1.48x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 44.7 ns: 1.45x faster                                  |
| chameleon               | 9.06 ms                                                | 6.27 ms: 1.45x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.41 ms: 1.44x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                  |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.40x faster                                 |
| logging_simple          | 8.07 us                                                | 5.78 us: 1.39x faster                                  |
| logging_format          | 8.91 us                                                | 6.39 us: 1.39x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.9 ms: 1.39x faster                                  |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                  |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.37x faster                                   |
| pprint_safe_repr        | 955 ms                                                 | 695 ms: 1.37x faster                                   |
| django_template         | 45.9 ms                                                | 33.5 ms: 1.37x faster                                  |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                  |
| genshi_xml              | 63.3 ms                                                | 46.7 ms: 1.36x faster                                  |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                  |
| deepcopy                | 442 us                                                 | 327 us: 1.35x faster                                   |
| tornado_http            | 127 ms                                                 | 94.6 ms: 1.35x faster                                  |
| fannkuch                | 486 ms                                                 | 362 ms: 1.34x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                 |
| thrift                  | 1.03 ms                                                | 777 us: 1.33x faster                                   |
| 2to3                    | 336 ms                                                 | 254 ms: 1.32x faster                                   |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.30x faster                                 |
| mypy2                   | 428 ms                                                 | 331 ms: 1.30x faster                                   |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.29x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.97 us: 1.29x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 665 ms: 1.28x faster                                   |
| nqueens                 | 100 ms                                                 | 78.8 ms: 1.27x faster                                  |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                 |
| coroutines              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 760 ms: 1.25x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 77.3 ms: 1.22x faster                                  |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                   |
| bench_thread_pool       | 947 us                                                 | 781 us: 1.21x faster                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                   |
| dulwich_log             | 75.9 ms                                                | 63.1 ms: 1.20x faster                                  |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                  |
| async_generators        | 425 ms                                                 | 356 ms: 1.20x faster                                   |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                   |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.19x faster                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.1 ms: 1.17x faster                                  |
| json                    | 5.42 ms                                                | 4.62 ms: 1.17x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                   |
| pickle_list             | 4.56 us                                                | 4.16 us: 1.09x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle                | 14.1 us                                                | 13.0 us: 1.08x faster                                  |
| regex_dna               | 222 ms                                                 | 211 ms: 1.05x faster                                   |
| mdp                     | 2.82 sec                                               | 2.73 sec: 1.03x faster                                 |
| telco                   | 6.54 ms                                                | 6.38 ms: 1.03x faster                                  |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                  |
| gc_traversal            | 3.84 ms                                                | 3.80 ms: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| unpickle_list           | 4.82 us                                                | 5.04 us: 1.05x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.44 ms: 1.07x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.12x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.2 us: 1.14x slower                                  |
| dask                    | 423 ms                                                 | 504 ms: 1.19x slower                                   |
| coverage                | 72.8 ms                                                | 95.3 ms: 1.31x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (2): generators, bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x

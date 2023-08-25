
# Results vs. 3.10.4

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: linux-x86_64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                  |
| chameleon      | 9.06 ms                                                | 6.46 ms: 1.40x faster                                                 |
| docutils       | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                |
| html5lib       | 85.9 ms                                                | 59.8 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.2 ms: 1.53x faster                                                 |
| nbody          | 142 ms                                                 | 93.1 ms: 1.52x faster                                                 |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                  |
| regex_v8       | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                 |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.49 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.54 ms: 1.42x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 53.9 ms: 1.39x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 77.5 ms: 1.22x faster                                                 |
| json_loads           | 28.8 us                                                | 24.3 us: 1.18x faster                                                 |
| pickle_list          | 4.56 us                                                | 4.02 us: 1.13x faster                                                 |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                  |
| unpickle             | 14.1 us                                                | 13.0 us: 1.09x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                  |
| pickle               | 10.3 us                                                | 10.0 us: 1.03x faster                                                 |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                                 |
| pickle_dict          | 27.3 us                                                | 30.0 us: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.54 ms: 1.66x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.09 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.74 ms: 1.52x faster                                                 |
| genshi_text     | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                 |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                 |
| genshi_xml      | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.25 ms: 2.28x faster                                                 |
| logging_silent          | 175 ns                                                 | 93.5 ns: 1.87x faster                                                 |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.84x faster                                                  |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                  |
| richards                | 74.9 ms                                                | 42.3 ms: 1.77x faster                                                 |
| pyflate                 | 673 ms                                                 | 397 ms: 1.70x faster                                                  |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.54 ms: 1.66x faster                                                 |
| scimark_monte_carlo     | 108 ms                                                 | 65.7 ms: 1.65x faster                                                 |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                                  |
| hexiom                  | 9.53 ms                                                | 5.98 ms: 1.59x faster                                                 |
| spectral_norm           | 150 ms                                                 | 95.0 ms: 1.58x faster                                                 |
| chaos                   | 106 ms                                                 | 67.7 ms: 1.57x faster                                                 |
| crypto_pyaes            | 118 ms                                                 | 75.7 ms: 1.56x faster                                                 |
| unpack_sequence         | 64.7 ns                                                | 41.4 ns: 1.56x faster                                                 |
| float                   | 111 ms                                                 | 72.2 ms: 1.53x faster                                                 |
| nbody                   | 142 ms                                                 | 93.1 ms: 1.52x faster                                                 |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.52x faster                                                  |
| mako                    | 14.8 ms                                                | 9.74 ms: 1.52x faster                                                 |
| deepcopy_memo           | 52.3 us                                                | 34.7 us: 1.51x faster                                                 |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                 |
| genshi_text             | 30.3 ms                                                | 20.8 ms: 1.46x faster                                                 |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                 |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                |
| html5lib                | 85.9 ms                                                | 59.8 ms: 1.44x faster                                                 |
| json_dumps              | 13.5 ms                                                | 9.54 ms: 1.42x faster                                                 |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                 |
| pprint_safe_repr        | 955 ms                                                 | 680 ms: 1.40x faster                                                  |
| logging_format          | 8.91 us                                                | 6.35 us: 1.40x faster                                                 |
| chameleon               | 9.06 ms                                                | 6.46 ms: 1.40x faster                                                 |
| logging_simple          | 8.07 us                                                | 5.77 us: 1.40x faster                                                 |
| xml_etree_process       | 74.9 ms                                                | 53.9 ms: 1.39x faster                                                 |
| pycparser               | 1.50 sec                                               | 1.08 sec: 1.39x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 616 ms: 1.39x faster                                                  |
| async_tree_none         | 717 ms                                                 | 521 ms: 1.38x faster                                                  |
| thrift                  | 1.03 ms                                                | 752 us: 1.37x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                |
| genshi_xml              | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                 |
| scimark_fft             | 424 ms                                                 | 314 ms: 1.35x faster                                                  |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                  |
| fannkuch                | 486 ms                                                 | 362 ms: 1.34x faster                                                  |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.13 ms: 1.32x faster                                                 |
| deepcopy                | 442 us                                                 | 339 us: 1.30x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                  |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                                 |
| nqueens                 | 100 ms                                                 | 78.0 ms: 1.28x faster                                                 |
| deepcopy_reduce         | 3.82 us                                                | 2.99 us: 1.28x faster                                                 |
| docutils                | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                |
| async_tree_cpu_io_mixed | 951 ms                                                 | 747 ms: 1.27x faster                                                  |
| coroutines              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                 |
| dulwich_log             | 75.9 ms                                                | 62.1 ms: 1.22x faster                                                 |
| xml_etree_generate      | 94.2 ms                                                | 77.5 ms: 1.22x faster                                                 |
| bench_thread_pool       | 947 us                                                 | 782 us: 1.21x faster                                                  |
| async_generators        | 425 ms                                                 | 354 ms: 1.20x faster                                                  |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                                 |
| dask                    | 423 ms                                                 | 355 ms: 1.19x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                 |
| json_loads              | 28.8 us                                                | 24.3 us: 1.18x faster                                                 |
| sympy_str               | 328 ms                                                 | 282 ms: 1.16x faster                                                  |
| djangocms               | 35.9 us                                                | 30.9 us: 1.16x faster                                                 |
| create_gc_cycles        | 1.67 ms                                                | 1.45 ms: 1.15x faster                                                 |
| json                    | 5.42 ms                                                | 4.74 ms: 1.14x faster                                                 |
| sqlite_synth            | 2.93 us                                                | 2.57 us: 1.14x faster                                                 |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                                  |
| pickle_list             | 4.56 us                                                | 4.02 us: 1.13x faster                                                 |
| comprehensions          | 26.8 us                                                | 23.7 us: 1.13x faster                                                 |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                 |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                  |
| unpickle                | 14.1 us                                                | 13.0 us: 1.09x faster                                                 |
| gc_traversal            | 3.84 ms                                                | 3.57 ms: 1.08x faster                                                 |
| regex_dna               | 222 ms                                                 | 209 ms: 1.06x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.66 sec: 1.06x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                  |
| telco                   | 6.54 ms                                                | 6.26 ms: 1.04x faster                                                 |
| pickle                  | 10.3 us                                                | 10.0 us: 1.03x faster                                                 |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                  |
| unpickle_list           | 4.82 us                                                | 4.96 us: 1.03x slower                                                 |
| generators              | 76.8 ms                                                | 79.1 ms: 1.03x slower                                                 |
| python_startup_no_site  | 5.82 ms                                                | 6.09 ms: 1.05x slower                                                 |
| regex_effbot            | 3.23 ms                                                | 3.49 ms: 1.08x slower                                                 |
| pickle_dict             | 27.3 us                                                | 30.0 us: 1.10x slower                                                 |
| coverage                | 72.8 ms                                                | 99.0 ms: 1.36x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

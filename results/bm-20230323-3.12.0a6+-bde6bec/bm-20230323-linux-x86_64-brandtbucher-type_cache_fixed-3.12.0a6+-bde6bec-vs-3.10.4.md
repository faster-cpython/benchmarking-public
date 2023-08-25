
# Results vs. 3.10.4

- fork: brandtbucher
- ref: type_cache_fixed
- machine: linux-x86_64
- commit hash: bde6bec
- commit date: 2023-03-23
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                     |
| chameleon      | 9.06 ms                                                | 6.55 ms: 1.38x faster                                                    |
| docutils       | 3.17 sec                                               | 2.56 sec: 1.24x faster                                                   |
| html5lib       | 85.9 ms                                                | 62.2 ms: 1.38x faster                                                    |
| tornado_http   | 127 ms                                                 | 92.7 ms: 1.37x faster                                                    |
| Geometric mean | (ref)                                                  | 1.34x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.2 ms: 1.57x faster                                                    |
| float          | 111 ms                                                 | 74.0 ms: 1.49x faster                                                    |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.33x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                     |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.12x faster                                                    |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                     |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                                     |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.49x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.53 ms: 1.42x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 56.5 ms: 1.33x faster                                                    |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 81.9 ms: 1.15x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                     |
| pickle_list          | 4.56 us                                                | 4.24 us: 1.07x faster                                                    |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                    |
| unpickle_list        | 4.82 us                                                | 5.07 us: 1.05x slower                                                    |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.83 ms: 1.60x faster                                                    |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.96 ms: 1.48x faster                                                    |
| genshi_text     | 30.3 ms                                                | 22.2 ms: 1.37x faster                                                    |
| django_template | 45.9 ms                                                | 33.8 ms: 1.36x faster                                                    |
| genshi_xml      | 63.3 ms                                                | 48.2 ms: 1.31x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-bde6bec |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.7 ms: 2.58x faster                                                    |
| deltablue               | 7.42 ms                                                | 3.40 ms: 2.18x faster                                                    |
| asyncio_tcp             | 925 ms                                                 | 509 ms: 1.82x faster                                                     |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.80x faster                                                     |
| logging_silent          | 175 ns                                                 | 98.4 ns: 1.78x faster                                                    |
| richards                | 74.9 ms                                                | 44.1 ms: 1.70x faster                                                    |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                     |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                                     |
| pyflate                 | 673 ms                                                 | 419 ms: 1.61x faster                                                     |
| python_startup          | 14.2 ms                                                | 8.83 ms: 1.60x faster                                                    |
| scimark_monte_carlo     | 108 ms                                                 | 67.6 ms: 1.60x faster                                                    |
| spectral_norm           | 150 ms                                                 | 94.3 ms: 1.59x faster                                                    |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                                     |
| crypto_pyaes            | 118 ms                                                 | 75.1 ms: 1.58x faster                                                    |
| nbody                   | 142 ms                                                 | 90.2 ms: 1.57x faster                                                    |
| chaos                   | 106 ms                                                 | 67.7 ms: 1.57x faster                                                    |
| unpack_sequence         | 64.7 ns                                                | 41.6 ns: 1.56x faster                                                    |
| hexiom                  | 9.53 ms                                                | 6.14 ms: 1.55x faster                                                    |
| deepcopy_memo           | 52.3 us                                                | 34.5 us: 1.52x faster                                                    |
| float                   | 111 ms                                                 | 74.0 ms: 1.49x faster                                                    |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.49x faster                                                     |
| mako                    | 14.8 ms                                                | 9.96 ms: 1.48x faster                                                    |
| scimark_lu              | 163 ms                                                 | 111 ms: 1.47x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.53 ms: 1.42x faster                                                    |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.47 ms: 1.40x faster                                                    |
| logging_format          | 8.91 us                                                | 6.40 us: 1.39x faster                                                    |
| sqlglot_transpile       | 2.45 ms                                                | 1.76 ms: 1.39x faster                                                    |
| pprint_safe_repr        | 955 ms                                                 | 690 ms: 1.38x faster                                                     |
| logging_simple          | 8.07 us                                                | 5.83 us: 1.38x faster                                                    |
| chameleon               | 9.06 ms                                                | 6.55 ms: 1.38x faster                                                    |
| coroutines              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                    |
| html5lib                | 85.9 ms                                                | 62.2 ms: 1.38x faster                                                    |
| tornado_http            | 127 ms                                                 | 92.7 ms: 1.37x faster                                                    |
| genshi_text             | 30.3 ms                                                | 22.2 ms: 1.37x faster                                                    |
| django_template         | 45.9 ms                                                | 33.8 ms: 1.36x faster                                                    |
| async_tree_none         | 717 ms                                                 | 531 ms: 1.35x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                   |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                     |
| scimark_fft             | 424 ms                                                 | 317 ms: 1.34x faster                                                     |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                     |
| gunicorn                | 1.46 ms                                                | 1.10 ms: 1.33x faster                                                    |
| xml_etree_process       | 74.9 ms                                                | 56.5 ms: 1.33x faster                                                    |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                     |
| genshi_xml              | 63.3 ms                                                | 48.2 ms: 1.31x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.24 ms: 1.29x faster                                                    |
| pycparser               | 1.50 sec                                               | 1.17 sec: 1.29x faster                                                   |
| thrift                  | 1.03 ms                                                | 806 us: 1.28x faster                                                     |
| fannkuch                | 486 ms                                                 | 379 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed | 951 ms                                                 | 748 ms: 1.27x faster                                                     |
| mypy2                   | 428 ms                                                 | 337 ms: 1.27x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 673 ms: 1.27x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 3.02 us: 1.27x faster                                                    |
| sqlglot_normalize       | 135 ms                                                 | 107 ms: 1.26x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 52.0 ms: 1.26x faster                                                    |
| docutils                | 3.17 sec                                               | 2.56 sec: 1.24x faster                                                   |
| nqueens                 | 100 ms                                                 | 81.9 ms: 1.22x faster                                                    |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                                    |
| bench_thread_pool       | 947 us                                                 | 796 us: 1.19x faster                                                     |
| dulwich_log             | 75.9 ms                                                | 64.1 ms: 1.19x faster                                                    |
| sympy_integrate         | 24.3 ms                                                | 20.6 ms: 1.18x faster                                                    |
| sympy_expand            | 545 ms                                                 | 467 ms: 1.17x faster                                                     |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                                    |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                                     |
| xml_etree_generate      | 94.2 ms                                                | 81.9 ms: 1.15x faster                                                    |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                    |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                    |
| comprehensions          | 26.8 us                                                | 23.9 us: 1.12x faster                                                    |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.12x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                     |
| mdp                     | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                   |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                     |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                    |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                     |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                                     |
| gc_traversal            | 3.84 ms                                                | 3.54 ms: 1.08x faster                                                    |
| pickle_list             | 4.56 us                                                | 4.24 us: 1.07x faster                                                    |
| async_generators        | 425 ms                                                 | 411 ms: 1.03x faster                                                     |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                     |
| telco                   | 6.54 ms                                                | 6.48 ms: 1.01x faster                                                    |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                    |
| unpickle_list           | 4.82 us                                                | 5.07 us: 1.05x slower                                                    |
| regex_effbot            | 3.23 ms                                                | 3.57 ms: 1.10x slower                                                    |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                    |
| pickle_dict             | 27.3 us                                                | 31.9 us: 1.17x slower                                                    |
| dask                    | 423 ms                                                 | 512 ms: 1.21x slower                                                     |
| coverage                | 72.8 ms                                                | 96.3 ms: 1.32x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                             |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

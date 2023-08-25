
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: cf0df30
- commit date: 2023-02-21
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 248 ms: 1.35x faster                                                       |
| chameleon      | 9.06 ms                                                | 6.38 ms: 1.42x faster                                                      |
| docutils       | 3.17 sec                                               | 2.60 sec: 1.22x faster                                                     |
| html5lib       | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                      |
| tornado_http   | 127 ms                                                 | 94.5 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.3 ms: 1.53x faster                                                      |
| nbody          | 142 ms                                                 | 94.2 ms: 1.50x faster                                                      |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                       |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                      |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                       |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 54.5 ms: 1.38x faster                                                      |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 80.0 ms: 1.18x faster                                                      |
| pickle_list          | 4.56 us                                                | 4.13 us: 1.10x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                       |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                                      |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                      |
| unpickle_list        | 4.82 us                                                | 5.03 us: 1.04x slower                                                      |
| pickle_dict          | 27.3 us                                                | 30.4 us: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.01 ms: 1.57x faster                                                      |
| python_startup_no_site | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                      |
| genshi_text     | 30.3 ms                                                | 20.6 ms: 1.48x faster                                                      |
| django_template | 45.9 ms                                                | 33.3 ms: 1.38x faster                                                      |
| genshi_xml      | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.9 ms: 2.57x faster                                                      |
| deltablue               | 7.42 ms                                                | 3.13 ms: 2.37x faster                                                      |
| logging_silent          | 175 ns                                                 | 91.0 ns: 1.92x faster                                                      |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                       |
| asyncio_tcp             | 925 ms                                                 | 502 ms: 1.84x faster                                                       |
| richards                | 74.9 ms                                                | 42.6 ms: 1.76x faster                                                      |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                                       |
| pyflate                 | 673 ms                                                 | 401 ms: 1.68x faster                                                       |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 72.3 ms: 1.64x faster                                                      |
| scimark_monte_carlo     | 108 ms                                                 | 66.9 ms: 1.62x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                                       |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.60x faster                                                      |
| spectral_norm           | 150 ms                                                 | 94.5 ms: 1.59x faster                                                      |
| hexiom                  | 9.53 ms                                                | 6.03 ms: 1.58x faster                                                      |
| python_startup          | 14.2 ms                                                | 9.01 ms: 1.57x faster                                                      |
| float                   | 111 ms                                                 | 72.3 ms: 1.53x faster                                                      |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                       |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                       |
| nbody                   | 142 ms                                                 | 94.2 ms: 1.50x faster                                                      |
| deepcopy_memo           | 52.3 us                                                | 35.2 us: 1.49x faster                                                      |
| mako                    | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                      |
| genshi_text             | 30.3 ms                                                | 20.6 ms: 1.48x faster                                                      |
| coroutines              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                                      |
| unpack_sequence         | 64.7 ns                                                | 44.7 ns: 1.45x faster                                                      |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                     |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                      |
| logging_format          | 8.91 us                                                | 6.26 us: 1.42x faster                                                      |
| chameleon               | 9.06 ms                                                | 6.38 ms: 1.42x faster                                                      |
| pprint_safe_repr        | 955 ms                                                 | 675 ms: 1.42x faster                                                       |
| html5lib                | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                      |
| logging_simple          | 8.07 us                                                | 5.75 us: 1.40x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 610 ms: 1.40x faster                                                       |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                      |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                       |
| django_template         | 45.9 ms                                                | 33.3 ms: 1.38x faster                                                      |
| async_tree_none         | 717 ms                                                 | 521 ms: 1.38x faster                                                       |
| xml_etree_process       | 74.9 ms                                                | 54.5 ms: 1.38x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                     |
| genshi_xml              | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                      |
| thrift                  | 1.03 ms                                                | 760 us: 1.36x faster                                                       |
| scimark_fft             | 424 ms                                                 | 312 ms: 1.36x faster                                                       |
| fannkuch                | 486 ms                                                 | 359 ms: 1.36x faster                                                       |
| 2to3                    | 336 ms                                                 | 248 ms: 1.35x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.03 ms: 1.35x faster                                                      |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                      |
| tornado_http            | 127 ms                                                 | 94.5 ms: 1.35x faster                                                      |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                                       |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                     |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                 | 735 ms: 1.29x faster                                                       |
| mypy2                   | 428 ms                                                 | 331 ms: 1.29x faster                                                       |
| nqueens                 | 100 ms                                                 | 77.5 ms: 1.29x faster                                                      |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                                      |
| deepcopy_reduce         | 3.82 us                                                | 2.98 us: 1.28x faster                                                      |
| docutils                | 3.17 sec                                               | 2.60 sec: 1.22x faster                                                     |
| dulwich_log             | 75.9 ms                                                | 63.0 ms: 1.20x faster                                                      |
| sympy_expand            | 545 ms                                                 | 452 ms: 1.20x faster                                                       |
| bench_thread_pool       | 947 us                                                 | 788 us: 1.20x faster                                                       |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                                      |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                                      |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                       |
| json                    | 5.42 ms                                                | 4.58 ms: 1.18x faster                                                      |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.18x faster                                                      |
| xml_etree_generate      | 94.2 ms                                                | 80.0 ms: 1.18x faster                                                      |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.45 sec: 1.15x faster                                                     |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                      |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                                       |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                      |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                      |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                      |
| pickle_list             | 4.56 us                                                | 4.13 us: 1.10x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| djangocms               | 35.9 us                                                | 32.8 us: 1.09x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                       |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                                      |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                       |
| gc_traversal            | 3.84 ms                                                | 3.61 ms: 1.07x faster                                                      |
| async_generators        | 425 ms                                                 | 407 ms: 1.04x faster                                                       |
| telco                   | 6.54 ms                                                | 6.42 ms: 1.02x faster                                                      |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                      |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                      |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                       |
| unpickle_list           | 4.82 us                                                | 5.03 us: 1.04x slower                                                      |
| pickle_dict             | 27.3 us                                                | 30.4 us: 1.11x slower                                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                      |
| regex_effbot            | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                      |
| dask                    | 423 ms                                                 | 497 ms: 1.18x slower                                                       |
| coverage                | 72.8 ms                                                | 97.2 ms: 1.33x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                               |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

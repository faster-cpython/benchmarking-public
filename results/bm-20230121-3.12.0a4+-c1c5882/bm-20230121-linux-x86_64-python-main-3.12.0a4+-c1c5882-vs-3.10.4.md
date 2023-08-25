
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c1c5882
- commit date: 2023-01-21
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 254 ms: 1.32x faster                                   |
| chameleon      | 9.06 ms                                                | 6.32 ms: 1.43x faster                                  |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                 |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                  |
| tornado_http   | 127 ms                                                 | 93.9 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.0 ms: 1.53x faster                                  |
| nbody          | 142 ms                                                 | 92.7 ms: 1.53x faster                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                  |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.65 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                   |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.39 ms: 1.44x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 54.1 ms: 1.39x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 78.1 ms: 1.21x faster                                  |
| json_loads           | 28.8 us                                                | 24.1 us: 1.19x faster                                  |
| pickle_list          | 4.56 us                                                | 4.01 us: 1.13x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                   |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                  |
| pickle               | 10.3 us                                                | 10.0 us: 1.03x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 159 ms: 1.03x faster                                   |
| unpickle_list        | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.3 us: 1.11x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.95 ms: 1.58x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.11x slower                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.90 ms: 1.49x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.1 ms: 1.44x faster                                  |
| django_template | 45.9 ms                                                | 32.3 ms: 1.42x faster                                  |
| genshi_xml      | 63.3 ms                                                | 47.3 ms: 1.34x faster                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.33x faster                                  |
| logging_silent          | 175 ns                                                 | 92.0 ns: 1.90x faster                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                   |
| asyncio_tcp             | 925 ms                                                 | 502 ms: 1.84x faster                                   |
| richards                | 74.9 ms                                                | 42.9 ms: 1.75x faster                                  |
| chaos                   | 106 ms                                                 | 62.4 ms: 1.70x faster                                  |
| pyflate                 | 673 ms                                                 | 398 ms: 1.69x faster                                   |
| go                      | 229 ms                                                 | 136 ms: 1.69x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 64.5 ms: 1.68x faster                                  |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 72.8 ms: 1.63x faster                                  |
| hexiom                  | 9.53 ms                                                | 5.88 ms: 1.62x faster                                  |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                   |
| python_startup          | 14.2 ms                                                | 8.95 ms: 1.58x faster                                  |
| spectral_norm           | 150 ms                                                 | 95.8 ms: 1.57x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 41.7 ns: 1.55x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 33.9 us: 1.54x faster                                  |
| float                   | 111 ms                                                 | 72.0 ms: 1.53x faster                                  |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.53x faster                                   |
| nbody                   | 142 ms                                                 | 92.7 ms: 1.53x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                   |
| mako                    | 14.8 ms                                                | 9.90 ms: 1.49x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                 |
| json_dumps              | 13.5 ms                                                | 9.39 ms: 1.44x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.1 ms: 1.44x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 665 ms: 1.44x faster                                   |
| chameleon               | 9.06 ms                                                | 6.32 ms: 1.43x faster                                  |
| django_template         | 45.9 ms                                                | 32.3 ms: 1.42x faster                                  |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                  |
| logging_format          | 8.91 us                                                | 6.34 us: 1.40x faster                                  |
| scimark_fft             | 424 ms                                                 | 302 ms: 1.40x faster                                   |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                   |
| aiohttp                 | 1.38 ms                                                | 996 us: 1.39x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 54.1 ms: 1.39x faster                                  |
| logging_simple          | 8.07 us                                                | 5.84 us: 1.38x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.97 ms: 1.37x faster                                  |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                  |
| deepcopy                | 442 us                                                 | 325 us: 1.36x faster                                   |
| tornado_http            | 127 ms                                                 | 93.9 ms: 1.36x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                 |
| genshi_xml              | 63.3 ms                                                | 47.3 ms: 1.34x faster                                  |
| fannkuch                | 486 ms                                                 | 364 ms: 1.34x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 645 ms: 1.32x faster                                   |
| 2to3                    | 336 ms                                                 | 254 ms: 1.32x faster                                   |
| nqueens                 | 100 ms                                                 | 76.0 ms: 1.32x faster                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.91 us: 1.31x faster                                  |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                 |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                   |
| coroutines              | 31.8 ms                                                | 24.6 ms: 1.30x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                  |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 755 ms: 1.26x faster                                   |
| async_generators        | 425 ms                                                 | 347 ms: 1.22x faster                                   |
| dulwich_log             | 75.9 ms                                                | 62.5 ms: 1.21x faster                                  |
| bench_thread_pool       | 947 us                                                 | 781 us: 1.21x faster                                   |
| sympy_expand            | 545 ms                                                 | 452 ms: 1.21x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 78.1 ms: 1.21x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.2 ms: 1.20x faster                                  |
| json_loads              | 28.8 us                                                | 24.1 us: 1.19x faster                                  |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                   |
| mdp                     | 2.82 sec                                               | 2.46 sec: 1.15x faster                                 |
| sqlite_synth            | 2.93 us                                                | 2.56 us: 1.15x faster                                  |
| json                    | 5.42 ms                                                | 4.73 ms: 1.15x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                  |
| pickle_list             | 4.56 us                                                | 4.01 us: 1.13x faster                                  |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                  |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                  |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                   |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                   |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                  |
| pickle                  | 10.3 us                                                | 10.0 us: 1.03x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 159 ms: 1.03x faster                                   |
| telco                   | 6.54 ms                                                | 6.39 ms: 1.02x faster                                  |
| generators              | 76.8 ms                                                | 76.6 ms: 1.00x faster                                  |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                  |
| gc_traversal            | 3.84 ms                                                | 3.88 ms: 1.01x slower                                  |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                   |
| unpickle_list           | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.3 us: 1.11x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.11x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.65 ms: 1.13x slower                                  |
| dask                    | 423 ms                                                 | 497 ms: 1.18x slower                                   |
| coverage                | 72.8 ms                                                | 96.0 ms: 1.32x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230121-3.12.0a4+-c1c5882/bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

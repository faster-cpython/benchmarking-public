
# Results vs. 3.10.4

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: 9595e01
- commit date: 2023-02-07
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                              |
| chameleon      | 9.06 ms                                                | 6.36 ms: 1.42x faster                                             |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                            |
| html5lib       | 85.9 ms                                                | 61.1 ms: 1.41x faster                                             |
| tornado_http   | 127 ms                                                 | 93.7 ms: 1.36x faster                                             |
| Geometric mean | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.7 ms: 1.50x faster                                             |
| nbody          | 142 ms                                                 | 96.0 ms: 1.48x faster                                             |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.29x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                              |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                             |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                              |
| regex_effbot   | 3.23 ms                                                | 3.62 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                              |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                              |
| json_dumps           | 13.5 ms                                                | 9.53 ms: 1.42x faster                                             |
| xml_etree_process    | 74.9 ms                                                | 53.2 ms: 1.41x faster                                             |
| xml_etree_generate   | 94.2 ms                                                | 77.4 ms: 1.22x faster                                             |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                             |
| pickle_list          | 4.56 us                                                | 4.14 us: 1.10x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                              |
| unpickle             | 14.1 us                                                | 13.3 us: 1.07x faster                                             |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                             |
| unpickle_list        | 4.82 us                                                | 5.01 us: 1.04x slower                                             |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.91 ms: 1.59x faster                                             |
| python_startup_no_site | 5.82 ms                                                | 6.47 ms: 1.11x slower                                             |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.92 ms: 1.49x faster                                             |
| genshi_text     | 30.3 ms                                                | 20.7 ms: 1.46x faster                                             |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                             |
| genshi_xml      | 63.3 ms                                                | 46.5 ms: 1.36x faster                                             |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.16 ms: 2.35x faster                                             |
| asyncio_tcp             | 925 ms                                                 | 492 ms: 1.88x faster                                              |
| logging_silent          | 175 ns                                                 | 93.3 ns: 1.88x faster                                             |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                              |
| richards                | 74.9 ms                                                | 42.2 ms: 1.77x faster                                             |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                              |
| pyflate                 | 673 ms                                                 | 404 ms: 1.67x faster                                              |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                              |
| scimark_monte_carlo     | 108 ms                                                 | 66.2 ms: 1.64x faster                                             |
| crypto_pyaes            | 118 ms                                                 | 72.6 ms: 1.63x faster                                             |
| chaos                   | 106 ms                                                 | 66.1 ms: 1.61x faster                                             |
| hexiom                  | 9.53 ms                                                | 5.96 ms: 1.60x faster                                             |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                              |
| python_startup          | 14.2 ms                                                | 8.91 ms: 1.59x faster                                             |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                             |
| unpack_sequence         | 64.7 ns                                                | 41.6 ns: 1.56x faster                                             |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                              |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                              |
| float                   | 111 ms                                                 | 73.7 ms: 1.50x faster                                             |
| deepcopy_memo           | 52.3 us                                                | 35.0 us: 1.50x faster                                             |
| mako                    | 14.8 ms                                                | 9.92 ms: 1.49x faster                                             |
| nbody                   | 142 ms                                                 | 96.0 ms: 1.48x faster                                             |
| genshi_text             | 30.3 ms                                                | 20.7 ms: 1.46x faster                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                             |
| chameleon               | 9.06 ms                                                | 6.36 ms: 1.42x faster                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.53 ms: 1.42x faster                                             |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.41x faster                                            |
| xml_etree_process       | 74.9 ms                                                | 53.2 ms: 1.41x faster                                             |
| thrift                  | 1.03 ms                                                | 735 us: 1.41x faster                                              |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                             |
| html5lib                | 85.9 ms                                                | 61.1 ms: 1.41x faster                                             |
| pprint_safe_repr        | 955 ms                                                 | 689 ms: 1.39x faster                                              |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                              |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                             |
| logging_format          | 8.91 us                                                | 6.48 us: 1.37x faster                                             |
| async_tree_none         | 717 ms                                                 | 522 ms: 1.37x faster                                              |
| logging_simple          | 8.07 us                                                | 5.89 us: 1.37x faster                                             |
| fannkuch                | 486 ms                                                 | 355 ms: 1.37x faster                                              |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                              |
| genshi_xml              | 63.3 ms                                                | 46.5 ms: 1.36x faster                                             |
| tornado_http            | 127 ms                                                 | 93.7 ms: 1.36x faster                                             |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.04 ms: 1.35x faster                                             |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                            |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                              |
| async_tree_memoization  | 854 ms                                                 | 647 ms: 1.32x faster                                              |
| deepcopy                | 442 us                                                 | 336 us: 1.32x faster                                              |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.30x faster                                            |
| mypy2                   | 428 ms                                                 | 330 ms: 1.30x faster                                              |
| coroutines              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                             |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                              |
| deepcopy_reduce         | 3.82 us                                                | 2.98 us: 1.28x faster                                             |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                             |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 757 ms: 1.26x faster                                              |
| nqueens                 | 100 ms                                                 | 81.0 ms: 1.23x faster                                             |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                             |
| async_generators        | 425 ms                                                 | 347 ms: 1.23x faster                                              |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                              |
| xml_etree_generate      | 94.2 ms                                                | 77.4 ms: 1.22x faster                                             |
| bench_thread_pool       | 947 us                                                 | 781 us: 1.21x faster                                              |
| dulwich_log             | 75.9 ms                                                | 63.0 ms: 1.21x faster                                             |
| sympy_expand            | 545 ms                                                 | 454 ms: 1.20x faster                                              |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                              |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.19x faster                                              |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                             |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.19x faster                                             |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                             |
| json                    | 5.42 ms                                                | 4.70 ms: 1.15x faster                                             |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                             |
| djangocms               | 35.9 us                                                | 31.7 us: 1.13x faster                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                             |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                             |
| pickle_list             | 4.56 us                                                | 4.14 us: 1.10x faster                                             |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                              |
| mdp                     | 2.82 sec                                               | 2.59 sec: 1.09x faster                                            |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                              |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                              |
| meteor_contest          | 115 ms                                                 | 108 ms: 1.07x faster                                              |
| unpickle                | 14.1 us                                                | 13.3 us: 1.07x faster                                             |
| generators              | 76.8 ms                                                | 75.7 ms: 1.01x faster                                             |
| telco                   | 6.54 ms                                                | 6.45 ms: 1.01x faster                                             |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                             |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                             |
| gc_traversal            | 3.84 ms                                                | 3.91 ms: 1.02x slower                                             |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                              |
| unpickle_list           | 4.82 us                                                | 5.01 us: 1.04x slower                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.47 ms: 1.11x slower                                             |
| regex_effbot            | 3.23 ms                                                | 3.62 ms: 1.12x slower                                             |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                             |
| coverage                | 72.8 ms                                                | 95.6 ms: 1.31x slower                                             |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                      |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x

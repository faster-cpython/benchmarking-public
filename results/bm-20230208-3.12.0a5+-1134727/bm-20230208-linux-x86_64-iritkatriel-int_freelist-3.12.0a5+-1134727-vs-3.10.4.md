
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 1134727
- commit date: 2023-02-08
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| chameleon      | 8.86 ms                                                | 6.30 ms: 1.41x faster                                               |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                              |
| html5lib       | 85.8 ms                                                | 61.0 ms: 1.41x faster                                               |
| tornado_http   | 128 ms                                                 | 94.2 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.4 ms: 1.51x faster                                               |
| nbody          | 136 ms                                                 | 95.0 ms: 1.43x faster                                               |
| pidigits       | 190 ms                                                 | 203 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.27x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| regex_dna      | 214 ms                                                 | 212 ms: 1.01x faster                                                |
| regex_effbot   | 3.21 ms                                                | 3.46 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 288 us: 1.58x faster                                                |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.51x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.60 ms: 1.40x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 55.1 ms: 1.35x faster                                               |
| json_loads           | 28.9 us                                                | 24.1 us: 1.20x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 80.4 ms: 1.16x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                               |
| pickle_list          | 4.50 us                                                | 4.22 us: 1.07x faster                                               |
| unpickle_list        | 4.99 us                                                | 4.89 us: 1.02x faster                                               |
| pickle               | 10.1 us                                                | 10.2 us: 1.00x slower                                               |
| pickle_dict          | 28.3 us                                                | 32.0 us: 1.13x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.92 ms: 1.56x faster                                               |
| python_startup_no_site | 5.76 ms                                                | 6.48 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                               |
| mako            | 14.3 ms                                                | 9.62 ms: 1.48x faster                                               |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                               |
| genshi_xml      | 63.6 ms                                                | 47.1 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.21 ms: 2.30x faster                                               |
| logging_silent          | 173 ns                                                 | 91.8 ns: 1.89x faster                                               |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                                |
| richards                | 71.4 ms                                                | 42.4 ms: 1.68x faster                                               |
| pyflate                 | 675 ms                                                 | 402 ms: 1.68x faster                                                |
| go                      | 226 ms                                                 | 135 ms: 1.68x faster                                                |
| scimark_monte_carlo     | 105 ms                                                 | 64.6 ms: 1.62x faster                                               |
| raytrace                | 461 ms                                                 | 285 ms: 1.62x faster                                                |
| chaos                   | 104 ms                                                 | 65.7 ms: 1.59x faster                                               |
| hexiom                  | 9.42 ms                                                | 5.96 ms: 1.58x faster                                               |
| pickle_pure_python      | 453 us                                                 | 288 us: 1.58x faster                                                |
| python_startup          | 13.9 ms                                                | 8.92 ms: 1.56x faster                                               |
| spectral_norm           | 148 ms                                                 | 95.2 ms: 1.56x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 76.5 ms: 1.54x faster                                               |
| float                   | 108 ms                                                 | 71.4 ms: 1.51x faster                                               |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.51x faster                                                |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                               |
| mako                    | 14.3 ms                                                | 9.62 ms: 1.48x faster                                               |
| deepcopy_memo           | 50.0 us                                                | 34.7 us: 1.44x faster                                               |
| scimark_lu              | 158 ms                                                 | 110 ms: 1.44x faster                                                |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.81 ms: 1.44x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                               |
| nbody                   | 136 ms                                                 | 95.0 ms: 1.43x faster                                               |
| pprint_pformat          | 1.97 sec                                               | 1.40 sec: 1.41x faster                                              |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.41x faster                                               |
| unpack_sequence         | 59.5 ns                                                | 42.2 ns: 1.41x faster                                               |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                               |
| chameleon               | 8.86 ms                                                | 6.30 ms: 1.41x faster                                               |
| html5lib                | 85.8 ms                                                | 61.0 ms: 1.41x faster                                               |
| logging_format          | 8.92 us                                                | 6.35 us: 1.41x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.60 ms: 1.40x faster                                               |
| scimark_fft             | 414 ms                                                 | 296 ms: 1.40x faster                                                |
| pprint_safe_repr        | 943 ms                                                 | 680 ms: 1.39x faster                                                |
| logging_simple          | 8.06 us                                                | 5.82 us: 1.38x faster                                               |
| thrift                  | 1.03 ms                                                | 755 us: 1.37x faster                                                |
| tornado_http            | 128 ms                                                 | 94.2 ms: 1.36x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 55.1 ms: 1.35x faster                                               |
| genshi_xml              | 63.6 ms                                                | 47.1 ms: 1.35x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                              |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                |
| async_tree_none         | 713 ms                                                 | 530 ms: 1.34x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                               |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                               |
| pycparser               | 1.51 sec                                               | 1.14 sec: 1.33x faster                                              |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| fannkuch                | 477 ms                                                 | 366 ms: 1.30x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 662 ms: 1.29x faster                                                |
| deepcopy                | 429 us                                                 | 334 us: 1.29x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                               |
| deepcopy_reduce         | 3.75 us                                                | 2.96 us: 1.27x faster                                               |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                              |
| nqueens                 | 99.3 ms                                                | 79.1 ms: 1.26x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 761 ms: 1.25x faster                                                |
| coroutines              | 31.7 ms                                                | 25.9 ms: 1.22x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                |
| dulwich_log             | 75.5 ms                                                | 62.3 ms: 1.21x faster                                               |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                               |
| bench_thread_pool       | 943 us                                                 | 785 us: 1.20x faster                                                |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                |
| json_loads              | 28.9 us                                                | 24.1 us: 1.20x faster                                               |
| sqlalchemy_imperative   | 21.0 ms                                                | 17.7 ms: 1.19x faster                                               |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.17x faster                                                |
| sympy_sum               | 183 ms                                                 | 157 ms: 1.17x faster                                                |
| xml_etree_generate      | 93.3 ms                                                | 80.4 ms: 1.16x faster                                               |
| json                    | 5.35 ms                                                | 4.63 ms: 1.16x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| sqlite_synth            | 2.90 us                                                | 2.56 us: 1.13x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| mdp                     | 2.82 sec                                               | 2.60 sec: 1.08x faster                                              |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                               |
| pickle_list             | 4.50 us                                                | 4.22 us: 1.07x faster                                               |
| meteor_contest          | 114 ms                                                 | 108 ms: 1.05x faster                                                |
| telco                   | 6.68 ms                                                | 6.50 ms: 1.03x faster                                               |
| unpickle_list           | 4.99 us                                                | 4.89 us: 1.02x faster                                               |
| regex_dna               | 214 ms                                                 | 212 ms: 1.01x faster                                                |
| async_generators        | 428 ms                                                 | 424 ms: 1.01x faster                                                |
| pickle                  | 10.1 us                                                | 10.2 us: 1.00x slower                                               |
| generators              | 75.8 ms                                                | 79.4 ms: 1.05x slower                                               |
| pidigits                | 190 ms                                                 | 203 ms: 1.06x slower                                                |
| regex_effbot            | 3.21 ms                                                | 3.46 ms: 1.08x slower                                               |
| python_startup_no_site  | 5.76 ms                                                | 6.48 ms: 1.12x slower                                               |
| pickle_dict             | 28.3 us                                                | 32.0 us: 1.13x slower                                               |
| coverage                | 75.3 ms                                                | 98.0 ms: 1.30x slower                                               |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230208-3.12.0a5+-1134727/bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2

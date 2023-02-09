
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 906fc0d
- commit date: 2023-01-30
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 253 ms: 1.31x faster                                                |
| chameleon      | 8.86 ms                                                | 6.31 ms: 1.40x faster                                               |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.28x faster                                              |
| html5lib       | 85.8 ms                                                | 60.3 ms: 1.42x faster                                               |
| tornado_http   | 128 ms                                                 | 93.9 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.1 ms: 1.49x faster                                               |
| nbody          | 136 ms                                                 | 95.5 ms: 1.43x faster                                               |
| pidigits       | 190 ms                                                 | 199 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.27x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                                |
| regex_effbot   | 3.21 ms                                                | 3.63 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 287 us: 1.58x faster                                                |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.50x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.58 ms: 1.41x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 77.6 ms: 1.20x faster                                               |
| json_loads           | 28.9 us                                                | 24.2 us: 1.19x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                               |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| pickle_list          | 4.50 us                                                | 4.24 us: 1.06x faster                                               |
| unpickle_list        | 4.99 us                                                | 4.89 us: 1.02x faster                                               |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                               |
| pickle_dict          | 28.3 us                                                | 31.2 us: 1.10x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.98 ms: 1.55x faster                                               |
| python_startup_no_site | 5.76 ms                                                | 6.49 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 21.0 ms: 1.46x faster                                               |
| mako            | 14.3 ms                                                | 9.87 ms: 1.44x faster                                               |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| genshi_xml      | 63.6 ms                                                | 47.6 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.20 ms: 2.31x faster                                               |
| logging_silent          | 173 ns                                                 | 92.2 ns: 1.88x faster                                               |
| scimark_sor             | 193 ms                                                 | 111 ms: 1.74x faster                                                |
| richards                | 71.4 ms                                                | 41.6 ms: 1.71x faster                                               |
| pyflate                 | 675 ms                                                 | 396 ms: 1.71x faster                                                |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                |
| chaos                   | 104 ms                                                 | 63.9 ms: 1.63x faster                                               |
| raytrace                | 461 ms                                                 | 289 ms: 1.60x faster                                                |
| hexiom                  | 9.42 ms                                                | 5.97 ms: 1.58x faster                                               |
| pickle_pure_python      | 453 us                                                 | 287 us: 1.58x faster                                                |
| scimark_monte_carlo     | 105 ms                                                 | 66.7 ms: 1.57x faster                                               |
| python_startup          | 13.9 ms                                                | 8.98 ms: 1.55x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 76.0 ms: 1.55x faster                                               |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.50x faster                                                |
| float                   | 108 ms                                                 | 72.1 ms: 1.49x faster                                               |
| scimark_lu              | 158 ms                                                 | 106 ms: 1.49x faster                                                |
| genshi_text             | 30.6 ms                                                | 21.0 ms: 1.46x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                               |
| mako                    | 14.3 ms                                                | 9.87 ms: 1.44x faster                                               |
| deepcopy_memo           | 50.0 us                                                | 34.6 us: 1.44x faster                                               |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                              |
| nbody                   | 136 ms                                                 | 95.5 ms: 1.43x faster                                               |
| html5lib                | 85.8 ms                                                | 60.3 ms: 1.42x faster                                               |
| logging_simple          | 8.06 us                                                | 5.68 us: 1.42x faster                                               |
| logging_format          | 8.92 us                                                | 6.30 us: 1.42x faster                                               |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.42x faster                                               |
| spectral_norm           | 148 ms                                                 | 105 ms: 1.42x faster                                                |
| pprint_safe_repr        | 943 ms                                                 | 669 ms: 1.41x faster                                                |
| json_dumps              | 13.5 ms                                                | 9.58 ms: 1.41x faster                                               |
| chameleon               | 8.86 ms                                                | 6.31 ms: 1.40x faster                                               |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                               |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                                |
| unpack_sequence         | 59.5 ns                                                | 43.3 ns: 1.37x faster                                               |
| tornado_http            | 128 ms                                                 | 93.9 ms: 1.37x faster                                               |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.02 ms: 1.37x faster                                               |
| async_tree_none         | 713 ms                                                 | 525 ms: 1.36x faster                                                |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| pycparser               | 1.51 sec                                               | 1.12 sec: 1.36x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                              |
| aiohttp                 | 1.34 ms                                                | 997 us: 1.34x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                               |
| genshi_xml              | 63.6 ms                                                | 47.6 ms: 1.33x faster                                               |
| scimark_fft             | 414 ms                                                 | 311 ms: 1.33x faster                                                |
| fannkuch                | 477 ms                                                 | 358 ms: 1.33x faster                                                |
| 2to3                    | 332 ms                                                 | 253 ms: 1.31x faster                                                |
| deepcopy                | 429 us                                                 | 330 us: 1.30x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 658 ms: 1.30x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                |
| deepcopy_reduce         | 3.75 us                                                | 2.94 us: 1.28x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                               |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.28x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 752 ms: 1.26x faster                                                |
| coroutines              | 31.7 ms                                                | 25.1 ms: 1.26x faster                                               |
| mypy                    | 1.01 sec                                               | 807 ms: 1.26x faster                                                |
| nqueens                 | 99.3 ms                                                | 79.5 ms: 1.25x faster                                               |
| async_generators        | 428 ms                                                 | 353 ms: 1.21x faster                                                |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                               |
| xml_etree_generate      | 93.3 ms                                                | 77.6 ms: 1.20x faster                                               |
| dulwich_log             | 75.5 ms                                                | 62.8 ms: 1.20x faster                                               |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                |
| bench_thread_pool       | 943 us                                                 | 790 us: 1.19x faster                                                |
| json_loads              | 28.9 us                                                | 24.2 us: 1.19x faster                                               |
| sympy_expand            | 537 ms                                                 | 453 ms: 1.18x faster                                                |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| json                    | 5.35 ms                                                | 4.67 ms: 1.15x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                               |
| sqlite_synth            | 2.90 us                                                | 2.60 us: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                               |
| mdp                     | 2.82 sec                                               | 2.62 sec: 1.08x faster                                              |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| meteor_contest          | 114 ms                                                 | 107 ms: 1.06x faster                                                |
| pickle_list             | 4.50 us                                                | 4.24 us: 1.06x faster                                               |
| telco                   | 6.68 ms                                                | 6.38 ms: 1.05x faster                                               |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                                |
| unpickle_list           | 4.99 us                                                | 4.89 us: 1.02x faster                                               |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                               |
| generators              | 75.8 ms                                                | 78.0 ms: 1.03x slower                                               |
| pidigits                | 190 ms                                                 | 199 ms: 1.05x slower                                                |
| pickle_dict             | 28.3 us                                                | 31.2 us: 1.10x slower                                               |
| python_startup_no_site  | 5.76 ms                                                | 6.49 ms: 1.13x slower                                               |
| regex_effbot            | 3.21 ms                                                | 3.63 ms: 1.13x slower                                               |
| coverage                | 75.3 ms                                                | 96.0 ms: 1.27x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230130-3.12.0a4+-906fc0d/bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal

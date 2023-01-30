
# Results vs. 3.10.4

- fork: python
- ref: b724ac2fe7fbb5a7a33d
- machine: linux-x86_64
- commit hash: b724ac2
- commit date: 2023-01-23
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 253 ms: 1.31x faster                                                   |
| chameleon      | 8.86 ms                                                | 6.42 ms: 1.38x faster                                                  |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                 |
| html5lib       | 85.8 ms                                                | 60.3 ms: 1.42x faster                                                  |
| tornado_http   | 128 ms                                                 | 93.7 ms: 1.37x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.6 ms: 1.48x faster                                                  |
| nbody          | 136 ms                                                 | 93.8 ms: 1.45x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                  |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                                   |
| regex_effbot   | 3.21 ms                                                | 3.44 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 284 us: 1.59x faster                                                   |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.50x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.38 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 54.4 ms: 1.37x faster                                                  |
| json_loads           | 28.9 us                                                | 24.3 us: 1.19x faster                                                  |
| xml_etree_generate   | 93.3 ms                                                | 79.1 ms: 1.18x faster                                                  |
| unpickle             | 14.3 us                                                | 13.4 us: 1.06x faster                                                  |
| pickle_list          | 4.50 us                                                | 4.26 us: 1.06x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                                   |
| unpickle_list        | 4.99 us                                                | 5.08 us: 1.02x slower                                                  |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                  |
| pickle_dict          | 28.3 us                                                | 32.2 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.96 ms: 1.55x faster                                                  |
| python_startup_no_site | 5.76 ms                                                | 6.49 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.66 ms: 1.48x faster                                                  |
| django_template | 46.3 ms                                                | 32.9 ms: 1.40x faster                                                  |
| genshi_text     | 30.6 ms                                                | 22.1 ms: 1.39x faster                                                  |
| genshi_xml      | 63.6 ms                                                | 46.8 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.23 ms: 2.29x faster                                                  |
| logging_silent          | 173 ns                                                 | 93.3 ns: 1.86x faster                                                  |
| scimark_sor             | 193 ms                                                 | 105 ms: 1.83x faster                                                   |
| pyflate                 | 675 ms                                                 | 400 ms: 1.69x faster                                                   |
| go                      | 226 ms                                                 | 136 ms: 1.67x faster                                                   |
| richards                | 71.4 ms                                                | 42.9 ms: 1.66x faster                                                  |
| raytrace                | 461 ms                                                 | 280 ms: 1.65x faster                                                   |
| chaos                   | 104 ms                                                 | 63.6 ms: 1.64x faster                                                  |
| scimark_monte_carlo     | 105 ms                                                 | 65.2 ms: 1.61x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 73.3 ms: 1.60x faster                                                  |
| pickle_pure_python      | 453 us                                                 | 284 us: 1.59x faster                                                   |
| hexiom                  | 9.42 ms                                                | 5.95 ms: 1.58x faster                                                  |
| python_startup          | 13.9 ms                                                | 8.96 ms: 1.55x faster                                                  |
| spectral_norm           | 148 ms                                                 | 97.7 ms: 1.52x faster                                                  |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.50x faster                                                   |
| float                   | 108 ms                                                 | 72.6 ms: 1.48x faster                                                  |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.48x faster                                                   |
| mako                    | 14.3 ms                                                | 9.66 ms: 1.48x faster                                                  |
| nbody                   | 136 ms                                                 | 93.8 ms: 1.45x faster                                                  |
| deepcopy_memo           | 50.0 us                                                | 34.6 us: 1.44x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.38 ms: 1.44x faster                                                  |
| unpack_sequence         | 59.5 ns                                                | 41.6 ns: 1.43x faster                                                  |
| pprint_pformat          | 1.97 sec                                               | 1.39 sec: 1.42x faster                                                 |
| html5lib                | 85.8 ms                                                | 60.3 ms: 1.42x faster                                                  |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.42x faster                                                  |
| logging_format          | 8.92 us                                                | 6.34 us: 1.41x faster                                                  |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.40x faster                                                  |
| logging_simple          | 8.06 us                                                | 5.74 us: 1.40x faster                                                  |
| pprint_safe_repr        | 943 ms                                                 | 674 ms: 1.40x faster                                                   |
| genshi_text             | 30.6 ms                                                | 22.1 ms: 1.39x faster                                                  |
| thrift                  | 1.03 ms                                                | 746 us: 1.38x faster                                                   |
| pycparser               | 1.51 sec                                               | 1.10 sec: 1.38x faster                                                 |
| chameleon               | 8.86 ms                                                | 6.42 ms: 1.38x faster                                                  |
| tornado_http            | 128 ms                                                 | 93.7 ms: 1.37x faster                                                  |
| xml_etree_process       | 74.5 ms                                                | 54.4 ms: 1.37x faster                                                  |
| genshi_xml              | 63.6 ms                                                | 46.8 ms: 1.36x faster                                                  |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.06 ms: 1.35x faster                                                  |
| scimark_fft             | 414 ms                                                 | 306 ms: 1.35x faster                                                   |
| async_tree_none         | 713 ms                                                 | 528 ms: 1.35x faster                                                   |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                   |
| aiohttp                 | 1.34 ms                                                | 994 us: 1.35x faster                                                   |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                  |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                 |
| fannkuch                | 477 ms                                                 | 363 ms: 1.32x faster                                                   |
| 2to3                    | 332 ms                                                 | 253 ms: 1.31x faster                                                   |
| deepcopy                | 429 us                                                 | 327 us: 1.31x faster                                                   |
| nqueens                 | 99.3 ms                                                | 76.2 ms: 1.30x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 666 ms: 1.28x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.3 ms: 1.27x faster                                                  |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                 |
| deepcopy_reduce         | 3.75 us                                                | 2.97 us: 1.26x faster                                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                   |
| mypy                    | 1.01 sec                                               | 810 ms: 1.25x faster                                                   |
| coroutines              | 31.7 ms                                                | 25.6 ms: 1.24x faster                                                  |
| dulwich_log             | 75.5 ms                                                | 62.0 ms: 1.22x faster                                                  |
| bench_thread_pool       | 943 us                                                 | 774 us: 1.22x faster                                                   |
| async_generators        | 428 ms                                                 | 351 ms: 1.22x faster                                                   |
| json_loads              | 28.9 us                                                | 24.3 us: 1.19x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                  |
| sympy_integrate         | 23.9 ms                                                | 20.2 ms: 1.18x faster                                                  |
| xml_etree_generate      | 93.3 ms                                                | 79.1 ms: 1.18x faster                                                  |
| sympy_expand            | 537 ms                                                 | 456 ms: 1.18x faster                                                   |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.43 sec: 1.16x faster                                                 |
| sympy_str               | 324 ms                                                 | 281 ms: 1.16x faster                                                   |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.13x faster                                                  |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                                   |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                   |
| unpickle                | 14.3 us                                                | 13.4 us: 1.06x faster                                                  |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                                   |
| pickle_list             | 4.50 us                                                | 4.26 us: 1.06x faster                                                  |
| telco                   | 6.68 ms                                                | 6.38 ms: 1.05x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.05x faster                                                   |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                                   |
| generators              | 75.8 ms                                                | 74.7 ms: 1.01x faster                                                  |
| unpickle_list           | 4.99 us                                                | 5.08 us: 1.02x slower                                                  |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| regex_effbot            | 3.21 ms                                                | 3.44 ms: 1.07x slower                                                  |
| python_startup_no_site  | 5.76 ms                                                | 6.49 ms: 1.13x slower                                                  |
| pickle_dict             | 28.3 us                                                | 32.2 us: 1.14x slower                                                  |
| coverage                | 75.3 ms                                                | 97.3 ms: 1.29x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230123-3.12.0a4+-b724ac2/bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal

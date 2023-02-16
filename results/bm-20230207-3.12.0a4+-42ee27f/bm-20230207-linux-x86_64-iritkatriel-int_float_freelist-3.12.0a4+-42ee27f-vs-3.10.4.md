
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_float_freelist
- machine: linux-x86_64
- commit hash: 42ee27f
- commit date: 2023-02-07
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                      |
| chameleon      | 9.17 ms                                                | 6.31 ms: 1.45x faster                                                     |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                    |
| html5lib       | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                     |
| tornado_http   | 128 ms                                                 | 94.0 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 109 ms                                                 | 72.5 ms: 1.50x faster                                                     |
| nbody          | 144 ms                                                 | 97.7 ms: 1.47x faster                                                     |
| pidigits       | 190 ms                                                 | 203 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.27x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                     |
| regex_dna      | 214 ms                                                 | 213 ms: 1.01x faster                                                      |
| regex_effbot   | 3.19 ms                                                | 3.43 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 284 us: 1.59x faster                                                      |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                      |
| json_dumps           | 13.4 ms                                                | 9.43 ms: 1.43x faster                                                     |
| xml_etree_process    | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                     |
| json_loads           | 28.7 us                                                | 23.7 us: 1.21x faster                                                     |
| xml_etree_generate   | 93.8 ms                                                | 77.9 ms: 1.20x faster                                                     |
| pickle_list          | 4.72 us                                                | 3.98 us: 1.19x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.08x faster                                                      |
| unpickle_list        | 4.92 us                                                | 4.84 us: 1.02x faster                                                     |
| pickle               | 10.2 us                                                | 9.98 us: 1.02x faster                                                     |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.97 ms: 1.57x faster                                                     |
| python_startup_no_site | 5.78 ms                                                | 6.49 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.63 ms: 1.52x faster                                                     |
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                     |
| django_template | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                     |
| genshi_xml      | 63.7 ms                                                | 47.5 ms: 1.34x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.26x faster                                                     |
| logging_silent          | 176 ns                                                 | 90.7 ns: 1.94x faster                                                     |
| asyncio_tcp             | 914 ms                                                 | 493 ms: 1.85x faster                                                      |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.85x faster                                                      |
| richards                | 75.2 ms                                                | 41.4 ms: 1.82x faster                                                     |
| pyflate                 | 676 ms                                                 | 394 ms: 1.72x faster                                                      |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                      |
| chaos                   | 106 ms                                                 | 63.9 ms: 1.65x faster                                                     |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                                      |
| scimark_monte_carlo     | 109 ms                                                 | 67.7 ms: 1.60x faster                                                     |
| pickle_pure_python      | 452 us                                                 | 284 us: 1.59x faster                                                      |
| spectral_norm           | 150 ms                                                 | 94.4 ms: 1.58x faster                                                     |
| hexiom                  | 9.43 ms                                                | 5.96 ms: 1.58x faster                                                     |
| python_startup          | 14.1 ms                                                | 8.97 ms: 1.57x faster                                                     |
| crypto_pyaes            | 117 ms                                                 | 75.9 ms: 1.54x faster                                                     |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                      |
| mako                    | 14.7 ms                                                | 9.63 ms: 1.52x faster                                                     |
| deepcopy_memo           | 51.7 us                                                | 34.2 us: 1.51x faster                                                     |
| float                   | 109 ms                                                 | 72.5 ms: 1.50x faster                                                     |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                     |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                      |
| nbody                   | 144 ms                                                 | 97.7 ms: 1.47x faster                                                     |
| chameleon               | 9.17 ms                                                | 6.31 ms: 1.45x faster                                                     |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                     |
| django_template         | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                     |
| logging_simple          | 8.10 us                                                | 5.64 us: 1.44x faster                                                     |
| json_dumps              | 13.4 ms                                                | 9.43 ms: 1.43x faster                                                     |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                                     |
| html5lib                | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                     |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                                    |
| logging_format          | 8.85 us                                                | 6.26 us: 1.41x faster                                                     |
| unpack_sequence         | 59.4 ns                                                | 42.1 ns: 1.41x faster                                                     |
| pprint_safe_repr        | 953 ms                                                 | 680 ms: 1.40x faster                                                      |
| thrift                  | 1.03 ms                                                | 740 us: 1.40x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                     |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                                    |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.99 ms: 1.37x faster                                                     |
| scimark_fft             | 421 ms                                                 | 308 ms: 1.37x faster                                                      |
| tornado_http            | 128 ms                                                 | 94.0 ms: 1.36x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                    |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                                      |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.35x faster                                                      |
| genshi_xml              | 63.7 ms                                                | 47.5 ms: 1.34x faster                                                     |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                                     |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                      |
| deepcopy                | 438 us                                                 | 331 us: 1.32x faster                                                      |
| deepcopy_reduce         | 3.79 us                                                | 2.91 us: 1.30x faster                                                     |
| async_tree_memoization  | 855 ms                                                 | 660 ms: 1.30x faster                                                      |
| fannkuch                | 488 ms                                                 | 377 ms: 1.29x faster                                                      |
| coroutines              | 31.6 ms                                                | 24.6 ms: 1.28x faster                                                     |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                                     |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                    |
| nqueens                 | 100 ms                                                 | 78.6 ms: 1.27x faster                                                     |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 761 ms: 1.25x faster                                                      |
| dulwich_log             | 75.8 ms                                                | 62.1 ms: 1.22x faster                                                     |
| bench_thread_pool       | 946 us                                                 | 780 us: 1.21x faster                                                      |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                                     |
| json_loads              | 28.7 us                                                | 23.7 us: 1.21x faster                                                     |
| async_generators        | 426 ms                                                 | 353 ms: 1.21x faster                                                      |
| xml_etree_generate      | 93.8 ms                                                | 77.9 ms: 1.20x faster                                                     |
| sympy_str               | 325 ms                                                 | 272 ms: 1.19x faster                                                      |
| pickle_list             | 4.72 us                                                | 3.98 us: 1.19x faster                                                     |
| json                    | 5.35 ms                                                | 4.56 ms: 1.17x faster                                                     |
| sympy_sum               | 183 ms                                                 | 157 ms: 1.17x faster                                                      |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                      |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                     |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                                     |
| sqlite_synth            | 2.92 us                                                | 2.57 us: 1.14x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                                     |
| mdp                     | 2.74 sec                                               | 2.45 sec: 1.12x faster                                                    |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.08x faster                                                      |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                      |
| telco                   | 6.73 ms                                                | 6.42 ms: 1.05x faster                                                     |
| unpickle_list           | 4.92 us                                                | 4.84 us: 1.02x faster                                                     |
| pickle                  | 10.2 us                                                | 9.98 us: 1.02x faster                                                     |
| regex_dna               | 214 ms                                                 | 213 ms: 1.01x faster                                                      |
| generators              | 76.4 ms                                                | 77.0 ms: 1.01x slower                                                     |
| gc_traversal            | 3.53 ms                                                | 3.59 ms: 1.02x slower                                                     |
| pidigits                | 190 ms                                                 | 203 ms: 1.07x slower                                                      |
| regex_effbot            | 3.19 ms                                                | 3.43 ms: 1.07x slower                                                     |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.12x slower                                                     |
| python_startup_no_site  | 5.78 ms                                                | 6.49 ms: 1.12x slower                                                     |
| dask                    | 436 ms                                                 | 495 ms: 1.13x slower                                                      |
| coverage                | 74.7 ms                                                | 97.1 ms: 1.30x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230207-3.12.0a4+-42ee27f/bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f.json: mypy

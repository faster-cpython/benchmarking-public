
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
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                      |
| chameleon      | 8.86 ms                                                | 6.31 ms: 1.40x faster                                                     |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                    |
| html5lib       | 85.8 ms                                                | 60.6 ms: 1.42x faster                                                     |
| tornado_http   | 128 ms                                                 | 94.0 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.5 ms: 1.49x faster                                                     |
| nbody          | 136 ms                                                 | 97.7 ms: 1.39x faster                                                     |
| pidigits       | 190 ms                                                 | 203 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.14x faster                                                     |
| regex_dna      | 214 ms                                                 | 213 ms: 1.01x faster                                                      |
| regex_effbot   | 3.21 ms                                                | 3.43 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 284 us: 1.60x faster                                                      |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.51x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.43 ms: 1.43x faster                                                     |
| xml_etree_process    | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                     |
| json_loads           | 28.9 us                                                | 23.7 us: 1.22x faster                                                     |
| xml_etree_generate   | 93.3 ms                                                | 77.9 ms: 1.20x faster                                                     |
| pickle_list          | 4.50 us                                                | 3.98 us: 1.13x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| unpickle             | 14.3 us                                                | 13.0 us: 1.10x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                      |
| unpickle_list        | 4.99 us                                                | 4.84 us: 1.03x faster                                                     |
| pickle               | 10.1 us                                                | 9.98 us: 1.01x faster                                                     |
| pickle_dict          | 28.3 us                                                | 30.8 us: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.97 ms: 1.55x faster                                                     |
| python_startup_no_site | 5.76 ms                                                | 6.49 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                     |
| mako            | 14.3 ms                                                | 9.63 ms: 1.48x faster                                                     |
| django_template | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                     |
| genshi_xml      | 63.6 ms                                                | 47.5 ms: 1.34x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.21 ms: 2.30x faster                                                     |
| logging_silent          | 173 ns                                                 | 90.7 ns: 1.91x faster                                                     |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                                      |
| richards                | 71.4 ms                                                | 41.4 ms: 1.72x faster                                                     |
| pyflate                 | 675 ms                                                 | 394 ms: 1.71x faster                                                      |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                      |
| chaos                   | 104 ms                                                 | 63.9 ms: 1.63x faster                                                     |
| raytrace                | 461 ms                                                 | 284 ms: 1.62x faster                                                      |
| pickle_pure_python      | 453 us                                                 | 284 us: 1.60x faster                                                      |
| hexiom                  | 9.42 ms                                                | 5.96 ms: 1.58x faster                                                     |
| spectral_norm           | 148 ms                                                 | 94.4 ms: 1.57x faster                                                     |
| python_startup          | 13.9 ms                                                | 8.97 ms: 1.55x faster                                                     |
| scimark_monte_carlo     | 105 ms                                                 | 67.7 ms: 1.55x faster                                                     |
| crypto_pyaes            | 118 ms                                                 | 75.9 ms: 1.55x faster                                                     |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.51x faster                                                      |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                     |
| float                   | 108 ms                                                 | 72.5 ms: 1.49x faster                                                     |
| mako                    | 14.3 ms                                                | 9.63 ms: 1.48x faster                                                     |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.47x faster                                                      |
| deepcopy_memo           | 50.0 us                                                | 34.2 us: 1.46x faster                                                     |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                     |
| django_template         | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.43 ms: 1.43x faster                                                     |
| logging_simple          | 8.06 us                                                | 5.64 us: 1.43x faster                                                     |
| logging_format          | 8.92 us                                                | 6.26 us: 1.43x faster                                                     |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                                     |
| html5lib                | 85.8 ms                                                | 60.6 ms: 1.42x faster                                                     |
| unpack_sequence         | 59.5 ns                                                | 42.1 ns: 1.41x faster                                                     |
| pprint_pformat          | 1.97 sec                                               | 1.40 sec: 1.41x faster                                                    |
| chameleon               | 8.86 ms                                                | 6.31 ms: 1.40x faster                                                     |
| nbody                   | 136 ms                                                 | 97.7 ms: 1.39x faster                                                     |
| thrift                  | 1.03 ms                                                | 740 us: 1.39x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                     |
| pprint_safe_repr        | 943 ms                                                 | 680 ms: 1.39x faster                                                      |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.99 ms: 1.37x faster                                                     |
| pycparser               | 1.51 sec                                               | 1.10 sec: 1.37x faster                                                    |
| tornado_http            | 128 ms                                                 | 94.0 ms: 1.36x faster                                                     |
| async_tree_none         | 713 ms                                                 | 527 ms: 1.35x faster                                                      |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                      |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                    |
| scimark_fft             | 414 ms                                                 | 308 ms: 1.34x faster                                                      |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.34x faster                                                      |
| genshi_xml              | 63.6 ms                                                | 47.5 ms: 1.34x faster                                                     |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                     |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                      |
| deepcopy                | 429 us                                                 | 331 us: 1.30x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 660 ms: 1.29x faster                                                      |
| deepcopy_reduce         | 3.75 us                                                | 2.91 us: 1.29x faster                                                     |
| coroutines              | 31.7 ms                                                | 24.6 ms: 1.29x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                     |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                    |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                      |
| fannkuch                | 477 ms                                                 | 377 ms: 1.26x faster                                                      |
| nqueens                 | 99.3 ms                                                | 78.6 ms: 1.26x faster                                                     |
| mypy                    | 1.01 sec                                               | 808 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 761 ms: 1.25x faster                                                      |
| json_loads              | 28.9 us                                                | 23.7 us: 1.22x faster                                                     |
| dulwich_log             | 75.5 ms                                                | 62.1 ms: 1.22x faster                                                     |
| async_generators        | 428 ms                                                 | 353 ms: 1.21x faster                                                      |
| bench_thread_pool       | 943 us                                                 | 780 us: 1.21x faster                                                      |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                                     |
| xml_etree_generate      | 93.3 ms                                                | 77.9 ms: 1.20x faster                                                     |
| sympy_str               | 324 ms                                                 | 272 ms: 1.19x faster                                                      |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.17x faster                                                      |
| json                    | 5.35 ms                                                | 4.56 ms: 1.17x faster                                                     |
| sympy_sum               | 183 ms                                                 | 157 ms: 1.17x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.45 sec: 1.15x faster                                                    |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.14x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                     |
| sqlite_synth            | 2.90 us                                                | 2.57 us: 1.13x faster                                                     |
| pickle_list             | 4.50 us                                                | 3.98 us: 1.13x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| unpickle                | 14.3 us                                                | 13.0 us: 1.10x faster                                                     |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                      |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                      |
| telco                   | 6.68 ms                                                | 6.42 ms: 1.04x faster                                                     |
| unpickle_list           | 4.99 us                                                | 4.84 us: 1.03x faster                                                     |
| pickle                  | 10.1 us                                                | 9.98 us: 1.01x faster                                                     |
| regex_dna               | 214 ms                                                 | 213 ms: 1.01x faster                                                      |
| generators              | 75.8 ms                                                | 77.0 ms: 1.02x slower                                                     |
| pidigits                | 190 ms                                                 | 203 ms: 1.07x slower                                                      |
| regex_effbot            | 3.21 ms                                                | 3.43 ms: 1.07x slower                                                     |
| pickle_dict             | 28.3 us                                                | 30.8 us: 1.09x slower                                                     |
| python_startup_no_site  | 5.76 ms                                                | 6.49 ms: 1.13x slower                                                     |
| coverage                | 75.3 ms                                                | 97.1 ms: 1.29x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230207-3.12.0a4+-42ee27f/bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal

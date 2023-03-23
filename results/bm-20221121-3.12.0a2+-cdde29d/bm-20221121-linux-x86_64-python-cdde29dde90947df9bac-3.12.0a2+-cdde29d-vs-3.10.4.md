
# Results vs. 3.10.4

- fork: python
- ref: cdde29dde90947df9bac
- machine: linux-x86_64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 244 ms: 1.37x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.31 ms: 1.45x faster                                                  |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                 |
| html5lib       | 85.9 ms                                                | 59.1 ms: 1.45x faster                                                  |
| tornado_http   | 128 ms                                                 | 92.8 ms: 1.38x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.7 ms: 1.54x faster                                                  |
| float          | 109 ms                                                 | 73.1 ms: 1.49x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                  |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.55 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 281 us: 1.61x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.51 ms: 1.41x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 52.8 ms: 1.41x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.3 ms: 1.23x faster                                                  |
| json_loads           | 28.7 us                                                | 23.8 us: 1.20x faster                                                  |
| pickle_list          | 4.72 us                                                | 3.97 us: 1.19x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| unpickle             | 14.2 us                                                | 13.6 us: 1.04x faster                                                  |
| pickle               | 10.2 us                                                | 10.4 us: 1.02x slower                                                  |
| unpickle_list        | 4.92 us                                                | 5.13 us: 1.04x slower                                                  |
| pickle_dict          | 27.6 us                                                | 31.3 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.48 ms: 1.66x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.12 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.56 ms: 1.53x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.2 ms: 1.52x faster                                                  |
| django_template | 46.3 ms                                                | 32.1 ms: 1.44x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 46.6 ms: 1.37x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.17 ms: 2.30x faster                                                  |
| logging_silent          | 176 ns                                                 | 94.1 ns: 1.87x faster                                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                   |
| richards                | 75.2 ms                                                | 41.3 ms: 1.82x faster                                                  |
| pyflate                 | 676 ms                                                 | 397 ms: 1.70x faster                                                   |
| go                      | 226 ms                                                 | 133 ms: 1.69x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 65.0 ms: 1.67x faster                                                  |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                                   |
| python_startup          | 14.1 ms                                                | 8.48 ms: 1.66x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 281 us: 1.61x faster                                                   |
| chaos                   | 106 ms                                                 | 65.6 ms: 1.61x faster                                                  |
| spectral_norm           | 150 ms                                                 | 95.6 ms: 1.56x faster                                                  |
| crypto_pyaes            | 117 ms                                                 | 75.1 ms: 1.55x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.32 ms: 1.54x faster                                                  |
| nbody                   | 144 ms                                                 | 93.7 ms: 1.54x faster                                                  |
| mako                    | 14.7 ms                                                | 9.56 ms: 1.53x faster                                                  |
| deepcopy_memo           | 51.7 us                                                | 33.8 us: 1.53x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.18 ms: 1.53x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                   |
| genshi_text             | 30.6 ms                                                | 20.2 ms: 1.52x faster                                                  |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.51x faster                                                   |
| sqlglot_transpile       | 2.43 ms                                                | 1.61 ms: 1.51x faster                                                  |
| float                   | 109 ms                                                 | 73.1 ms: 1.49x faster                                                  |
| html5lib                | 85.9 ms                                                | 59.1 ms: 1.45x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.31 ms: 1.45x faster                                                  |
| django_template         | 46.3 ms                                                | 32.1 ms: 1.44x faster                                                  |
| logging_simple          | 8.10 us                                                | 5.62 us: 1.44x faster                                                  |
| pycparser               | 1.53 sec                                               | 1.07 sec: 1.43x faster                                                 |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.43x faster                                                 |
| json_dumps              | 13.4 ms                                                | 9.51 ms: 1.41x faster                                                  |
| xml_etree_process       | 74.5 ms                                                | 52.8 ms: 1.41x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 676 ms: 1.41x faster                                                   |
| logging_format          | 8.85 us                                                | 6.29 us: 1.41x faster                                                  |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                   |
| thrift                  | 1.03 ms                                                | 748 us: 1.38x faster                                                   |
| tornado_http            | 128 ms                                                 | 92.8 ms: 1.38x faster                                                  |
| async_tree_memoization  | 855 ms                                                 | 622 ms: 1.38x faster                                                   |
| 2to3                    | 335 ms                                                 | 244 ms: 1.37x faster                                                   |
| scimark_fft             | 421 ms                                                 | 307 ms: 1.37x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 46.6 ms: 1.37x faster                                                  |
| aiohttp                 | 1.34 ms                                                | 991 us: 1.35x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                 |
| async_tree_none         | 711 ms                                                 | 530 ms: 1.34x faster                                                   |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.08 ms: 1.34x faster                                                  |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                                   |
| unpack_sequence         | 59.4 ns                                                | 45.1 ns: 1.32x faster                                                  |
| fannkuch                | 488 ms                                                 | 373 ms: 1.31x faster                                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.2 ms: 1.30x faster                                                  |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.30x faster                                                   |
| coroutines              | 31.6 ms                                                | 24.5 ms: 1.29x faster                                                  |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                 |
| deepcopy_reduce         | 3.79 us                                                | 2.99 us: 1.27x faster                                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                   |
| dulwich_log             | 75.8 ms                                                | 61.5 ms: 1.23x faster                                                  |
| xml_etree_generate      | 93.8 ms                                                | 76.3 ms: 1.23x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 774 us: 1.22x faster                                                   |
| nqueens                 | 100 ms                                                 | 82.0 ms: 1.22x faster                                                  |
| json_loads              | 28.7 us                                                | 23.8 us: 1.20x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                  |
| async_generators        | 426 ms                                                 | 358 ms: 1.19x faster                                                   |
| pickle_list             | 4.72 us                                                | 3.97 us: 1.19x faster                                                  |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.18x faster                                                  |
| sympy_expand            | 534 ms                                                 | 454 ms: 1.18x faster                                                   |
| sympy_str               | 325 ms                                                 | 280 ms: 1.16x faster                                                   |
| json                    | 5.35 ms                                                | 4.61 ms: 1.16x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                  |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.13x faster                                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                  |
| meteor_contest          | 114 ms                                                 | 102 ms: 1.12x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| telco                   | 6.73 ms                                                | 6.44 ms: 1.04x faster                                                  |
| unpickle                | 14.2 us                                                | 13.6 us: 1.04x faster                                                  |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                                   |
| mdp                     | 2.74 sec                                               | 2.69 sec: 1.02x faster                                                 |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| generators              | 76.4 ms                                                | 77.7 ms: 1.02x slower                                                  |
| pickle                  | 10.2 us                                                | 10.4 us: 1.02x slower                                                  |
| unpickle_list           | 4.92 us                                                | 5.13 us: 1.04x slower                                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.12 ms: 1.06x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.55 ms: 1.11x slower                                                  |
| pickle_dict             | 27.6 us                                                | 31.3 us: 1.14x slower                                                  |
| coverage                | 74.7 ms                                                | 102 ms: 1.36x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221121-3.12.0a2+-cdde29d/bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d.json: mypy

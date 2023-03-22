
# Results vs. 3.10.4

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: darwin-arm64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.17x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 186 ms: 1.08x faster                                                  |
| chameleon      | 5.79 ms                                                | 5.09 ms: 1.14x faster                                                 |
| docutils       | 1.78 sec                                               | 1.53 sec: 1.16x faster                                                |
| html5lib       | 44.2 ms                                                | 36.5 ms: 1.21x faster                                                 |
| tornado_http   | 91.5 ms                                                | 75.9 ms: 1.21x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.6 ms: 1.40x faster                                                 |
| nbody          | 93.3 ms                                                | 74.0 ms: 1.26x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 77.9 ms: 1.24x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.47 ms: 1.00x slower                                                 |
| regex_dna      | 162 ms                                                 | 164 ms: 1.02x slower                                                  |
| regex_v8       | 17.6 ms                                                | 18.1 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 227 us: 1.25x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 36.8 ms: 1.22x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 174 us: 1.17x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.7 ms: 1.11x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 95.7 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 66.5 ms: 1.09x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.80 ms: 1.08x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.52 us: 1.06x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.7 us: 1.01x faster                                                 |
| pickle               | 7.35 us                                                | 7.28 us: 1.01x faster                                                 |
| json_loads           | 16.9 us                                                | 16.8 us: 1.01x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.84 us: 1.01x slower                                                 |
| unpickle             | 9.89 us                                                | 10.0 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.88 ms                                                | 7.30 ms: 1.22x faster                                                 |
| python_startup         | 11.9 ms                                                | 13.6 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 8.49 ms: 1.23x faster                                                 |
| django_template | 27.3 ms                                                | 22.7 ms: 1.20x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 31.1 ms: 1.19x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.7 ms: 1.17x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 3.19 ms: 1.61x faster                                                 |
| raytrace                | 325 ms                                                 | 208 ms: 1.56x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 48.8 ms: 1.49x faster                                                 |
| logging_silent          | 119 ns                                                 | 82.6 ns: 1.45x faster                                                 |
| pathlib                 | 28.8 ms                                                | 20.5 ms: 1.41x faster                                                 |
| float                   | 72.4 ms                                                | 51.6 ms: 1.40x faster                                                 |
| go                      | 165 ms                                                 | 119 ms: 1.40x faster                                                  |
| async_tree_none         | 400 ms                                                 | 290 ms: 1.38x faster                                                  |
| richards                | 51.4 ms                                                | 37.4 ms: 1.38x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 360 ms: 1.36x faster                                                  |
| chaos                   | 66.7 ms                                                | 49.0 ms: 1.36x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 58.1 ms: 1.34x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.45 us: 1.34x faster                                                 |
| logging_format          | 4.97 us                                                | 3.72 us: 1.34x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 779 ms: 1.31x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.91 ms: 1.29x faster                                                 |
| spectral_norm           | 95.8 ms                                                | 75.0 ms: 1.28x faster                                                 |
| scimark_sor             | 126 ms                                                 | 98.8 ms: 1.28x faster                                                 |
| nbody                   | 93.3 ms                                                | 74.0 ms: 1.26x faster                                                 |
| pyflate                 | 453 ms                                                 | 361 ms: 1.25x faster                                                  |
| thrift                  | 580 us                                                 | 465 us: 1.25x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 227 us: 1.25x faster                                                  |
| regex_compile           | 96.4 ms                                                | 77.9 ms: 1.24x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 27.8 us: 1.24x faster                                                 |
| mako                    | 10.5 ms                                                | 8.49 ms: 1.23x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 30.0 ms: 1.23x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 36.8 ms: 1.22x faster                                                 |
| python_startup_no_site  | 8.88 ms                                                | 7.30 ms: 1.22x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 500 ms: 1.21x faster                                                  |
| html5lib                | 44.2 ms                                                | 36.5 ms: 1.21x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 1.02 sec: 1.21x faster                                                |
| tornado_http            | 91.5 ms                                                | 75.9 ms: 1.21x faster                                                 |
| django_template         | 27.3 ms                                                | 22.7 ms: 1.20x faster                                                 |
| unpack_sequence         | 37.4 ns                                                | 31.2 ns: 1.20x faster                                                 |
| pycparser               | 916 ms                                                 | 766 ms: 1.20x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 31.1 ms: 1.19x faster                                                 |
| gunicorn                | 1.35 ms                                                | 1.13 ms: 1.19x faster                                                 |
| async_generators        | 234 ms                                                 | 197 ms: 1.19x faster                                                  |
| deepcopy                | 281 us                                                 | 237 us: 1.18x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.7 ms: 1.17x faster                                                 |
| deepcopy_reduce         | 2.37 us                                                | 2.04 us: 1.17x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 174 us: 1.17x faster                                                  |
| scimark_lu              | 109 ms                                                 | 93.9 ms: 1.16x faster                                                 |
| docutils                | 1.78 sec                                               | 1.53 sec: 1.16x faster                                                |
| generators              | 32.7 ms                                                | 28.2 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 579 ms: 1.16x faster                                                  |
| scimark_fft             | 230 ms                                                 | 202 ms: 1.14x faster                                                  |
| chameleon               | 5.79 ms                                                | 5.09 ms: 1.14x faster                                                 |
| fannkuch                | 317 ms                                                 | 280 ms: 1.13x faster                                                  |
| sqlglot_optimize        | 38.0 ms                                                | 33.5 ms: 1.13x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 174 ms: 1.13x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.40 ms: 1.13x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.23 ms: 1.11x faster                                                 |
| nqueens                 | 68.2 ms                                                | 61.3 ms: 1.11x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 48.7 ms: 1.11x faster                                                 |
| pylint                  | 307 ms                                                 | 276 ms: 1.11x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 95.7 ms: 1.11x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 496 us: 1.10x faster                                                  |
| sympy_integrate         | 13.3 ms                                                | 12.1 ms: 1.09x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 86.0 ms: 1.09x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 66.5 ms: 1.09x faster                                                 |
| sympy_expand            | 275 ms                                                 | 254 ms: 1.08x faster                                                  |
| 2to3                    | 201 ms                                                 | 186 ms: 1.08x faster                                                  |
| sympy_str               | 169 ms                                                 | 157 ms: 1.08x faster                                                  |
| json_dumps              | 8.40 ms                                                | 7.80 ms: 1.08x faster                                                 |
| telco                   | 3.63 ms                                                | 3.40 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.24 ms: 1.07x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.52 us: 1.06x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.56 sec: 1.06x faster                                                |
| sqlite_synth            | 1.47 us                                                | 1.39 us: 1.06x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 74.3 ms: 1.05x faster                                                 |
| coroutines              | 20.2 ms                                                | 19.2 ms: 1.05x faster                                                 |
| json                    | 3.08 ms                                                | 3.03 ms: 1.02x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.7 us: 1.01x faster                                                 |
| pickle                  | 7.35 us                                                | 7.28 us: 1.01x faster                                                 |
| json_loads              | 16.9 us                                                | 16.8 us: 1.01x faster                                                 |
| pidigits                | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_effbot            | 2.46 ms                                                | 2.47 ms: 1.00x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.84 us: 1.01x slower                                                 |
| unpickle                | 9.89 us                                                | 10.0 us: 1.01x slower                                                 |
| regex_dna               | 162 ms                                                 | 164 ms: 1.02x slower                                                  |
| coverage                | 42.0 ms                                                | 43.0 ms: 1.02x slower                                                 |
| regex_v8                | 17.6 ms                                                | 18.1 ms: 1.03x slower                                                 |
| python_startup          | 11.9 ms                                                | 13.6 ms: 1.14x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (2): flaskblogging, bench_mp_pool
Ignored benchmarks (9) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative

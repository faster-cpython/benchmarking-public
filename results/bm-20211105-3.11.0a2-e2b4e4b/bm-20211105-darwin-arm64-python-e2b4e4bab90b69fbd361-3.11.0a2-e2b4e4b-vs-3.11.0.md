
# Results vs. 3.11.0

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: darwin-arm64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.04x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 186 ms: 1.16x slower                                                  |
| chameleon      | 4.57 ms                                                | 5.09 ms: 1.11x slower                                                 |
| docutils       | 1.47 sec                                               | 1.53 sec: 1.04x slower                                                |
| html5lib       | 34.7 ms                                                | 36.5 ms: 1.05x slower                                                 |
| tornado_http   | 72.4 ms                                                | 75.9 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.6 ms: 1.03x faster                                                 |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| nbody          | 65.5 ms                                                | 74.0 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.07x faster                                                 |
| regex_compile  | 76.7 ms                                                | 77.9 ms: 1.02x slower                                                 |
| regex_dna      | 152 ms                                                 | 164 ms: 1.08x slower                                                  |
| regex_v8       | 16.2 ms                                                | 18.1 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 95.7 ms: 1.11x faster                                                 |
| unpickle_list        | 2.63 us                                                | 2.52 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 66.5 ms: 1.04x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.7 us: 1.01x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 48.7 ms: 1.00x faster                                                 |
| json_dumps           | 7.72 ms                                                | 7.80 ms: 1.01x slower                                                 |
| pickle_list          | 2.81 us                                                | 2.84 us: 1.01x slower                                                 |
| pickle               | 7.17 us                                                | 7.28 us: 1.02x slower                                                 |
| unpickle             | 9.70 us                                                | 10.0 us: 1.03x slower                                                 |
| json_loads           | 16.1 us                                                | 16.8 us: 1.04x slower                                                 |
| xml_etree_process    | 35.2 ms                                                | 36.8 ms: 1.05x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 174 us: 1.10x slower                                                  |
| pickle_pure_python   | 199 us                                                 | 227 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.30 ms: 1.27x faster                                                 |
| python_startup         | 11.5 ms                                                | 13.6 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 15.3 ms                                                | 15.7 ms: 1.03x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 31.1 ms: 1.04x slower                                                 |
| django_template | 21.0 ms                                                | 22.7 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coverage                | 58.6 ms                                                | 43.0 ms: 1.36x faster                                                 |
| pathlib                 | 27.8 ms                                                | 20.5 ms: 1.36x faster                                                 |
| python_startup_no_site  | 9.31 ms                                                | 7.30 ms: 1.27x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 95.7 ms: 1.11x faster                                                 |
| bench_mp_pool           | 43.2 ms                                                | 39.9 ms: 1.08x faster                                                 |
| unpack_sequence         | 33.6 ns                                                | 31.2 ns: 1.08x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.47 ms: 1.07x faster                                                 |
| unpickle_list           | 2.63 us                                                | 2.52 us: 1.04x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 66.5 ms: 1.04x faster                                                 |
| float                   | 53.0 ms                                                | 51.6 ms: 1.03x faster                                                 |
| generators              | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                 |
| logging_simple          | 3.50 us                                                | 3.45 us: 1.02x faster                                                 |
| logging_format          | 3.78 us                                                | 3.72 us: 1.02x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.7 us: 1.01x faster                                                 |
| chaos                   | 49.5 ms                                                | 49.0 ms: 1.01x faster                                                 |
| xml_etree_generate      | 48.8 ms                                                | 48.7 ms: 1.00x faster                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| dulwich_log             | 29.9 ms                                                | 30.0 ms: 1.01x slower                                                 |
| raytrace                | 207 ms                                                 | 208 ms: 1.01x slower                                                  |
| meteor_contest          | 73.8 ms                                                | 74.3 ms: 1.01x slower                                                 |
| json_dumps              | 7.72 ms                                                | 7.80 ms: 1.01x slower                                                 |
| async_generators        | 195 ms                                                 | 197 ms: 1.01x slower                                                  |
| scimark_fft             | 199 ms                                                 | 202 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.24 ms: 1.01x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.84 us: 1.01x slower                                                 |
| mdp                     | 1.54 sec                                               | 1.56 sec: 1.01x slower                                                |
| pickle                  | 7.17 us                                                | 7.28 us: 1.02x slower                                                 |
| regex_compile           | 76.7 ms                                                | 77.9 ms: 1.02x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                  |
| async_tree_none         | 285 ms                                                 | 290 ms: 1.02x slower                                                  |
| genshi_text             | 15.3 ms                                                | 15.7 ms: 1.03x slower                                                 |
| spectral_norm           | 72.8 ms                                                | 75.0 ms: 1.03x slower                                                 |
| unpickle                | 9.70 us                                                | 10.0 us: 1.03x slower                                                 |
| sympy_str               | 152 ms                                                 | 157 ms: 1.04x slower                                                  |
| hexiom                  | 4.73 ms                                                | 4.91 ms: 1.04x slower                                                 |
| docutils                | 1.47 sec                                               | 1.53 sec: 1.04x slower                                                |
| json_loads              | 16.1 us                                                | 16.8 us: 1.04x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 31.1 ms: 1.04x slower                                                 |
| xml_etree_process       | 35.2 ms                                                | 36.8 ms: 1.05x slower                                                 |
| sympy_expand            | 243 ms                                                 | 254 ms: 1.05x slower                                                  |
| tornado_http            | 72.4 ms                                                | 75.9 ms: 1.05x slower                                                 |
| bench_thread_pool       | 473 us                                                 | 496 us: 1.05x slower                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 48.8 ms: 1.05x slower                                                 |
| html5lib                | 34.7 ms                                                | 36.5 ms: 1.05x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 27.8 us: 1.06x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 12.1 ms: 1.06x slower                                                 |
| deepcopy                | 224 us                                                 | 237 us: 1.06x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.04 us: 1.07x slower                                                 |
| fannkuch                | 261 ms                                                 | 280 ms: 1.07x slower                                                  |
| thrift                  | 433 us                                                 | 465 us: 1.07x slower                                                  |
| pprint_pformat          | 950 ms                                                 | 1.02 sec: 1.07x slower                                                |
| async_tree_memoization  | 336 ms                                                 | 360 ms: 1.07x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                | 33.5 ms: 1.08x slower                                                 |
| pprint_safe_repr        | 465 ms                                                 | 500 ms: 1.08x slower                                                  |
| django_template         | 21.0 ms                                                | 22.7 ms: 1.08x slower                                                 |
| async_tree_cpu_io_mixed | 534 ms                                                 | 579 ms: 1.08x slower                                                  |
| coroutines              | 17.7 ms                                                | 19.2 ms: 1.08x slower                                                 |
| regex_dna               | 152 ms                                                 | 164 ms: 1.08x slower                                                  |
| go                      | 109 ms                                                 | 119 ms: 1.09x slower                                                  |
| json                    | 2.77 ms                                                | 3.03 ms: 1.09x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.39 us: 1.09x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 174 us: 1.10x slower                                                  |
| pycparser               | 697 ms                                                 | 766 ms: 1.10x slower                                                  |
| async_tree_io           | 706 ms                                                 | 779 ms: 1.10x slower                                                  |
| chameleon               | 4.57 ms                                                | 5.09 ms: 1.11x slower                                                 |
| regex_v8                | 16.2 ms                                                | 18.1 ms: 1.12x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 58.1 ms: 1.12x slower                                                 |
| nbody                   | 65.5 ms                                                | 74.0 ms: 1.13x slower                                                 |
| deltablue               | 2.81 ms                                                | 3.19 ms: 1.14x slower                                                 |
| flaskblogging           | 2.42 ms                                                | 2.76 ms: 1.14x slower                                                 |
| pickle_pure_python      | 199 us                                                 | 227 us: 1.14x slower                                                  |
| 2to3                    | 161 ms                                                 | 186 ms: 1.16x slower                                                  |
| richards                | 32.2 ms                                                | 37.4 ms: 1.16x slower                                                 |
| pyflate                 | 311 ms                                                 | 361 ms: 1.16x slower                                                  |
| python_startup          | 11.5 ms                                                | 13.6 ms: 1.18x slower                                                 |
| scimark_sor             | 83.0 ms                                                | 98.8 ms: 1.19x slower                                                 |
| logging_silent          | 68.0 ns                                                | 82.6 ns: 1.22x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.40 ms: 1.25x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.23 ms: 1.28x slower                                                 |
| scimark_lu              | 72.1 ms                                                | 93.9 ms: 1.30x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (6): nqueens, gunicorn, sympy_sum, mako, telco, pylint
Ignored benchmarks (9) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative

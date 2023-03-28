
# Results vs. 3.10.4

- fork: python
- ref: f9774e57d84162ff0cba
- machine: darwin-arm64
- commit hash: f9774e5
- commit date: 2023-03-07
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 165 ms: 1.22x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.48 ms: 1.29x faster                                                 |
| docutils       | 1.78 sec                                               | 1.49 sec: 1.19x faster                                                |
| html5lib       | 44.2 ms                                                | 35.4 ms: 1.25x faster                                                 |
| tornado_http   | 91.5 ms                                                | 70.0 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 66.1 ms: 1.41x faster                                                 |
| float          | 72.4 ms                                                | 53.5 ms: 1.35x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 75.4 ms: 1.28x faster                                                 |
| regex_v8       | 17.6 ms                                                | 16.2 ms: 1.08x faster                                                 |
| regex_dna      | 162 ms                                                 | 153 ms: 1.05x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.69 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 191 us: 1.49x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.40x faster                                                  |
| json_dumps           | 8.40 ms                                                | 6.18 ms: 1.36x faster                                                 |
| xml_etree_process    | 44.8 ms                                                | 37.0 ms: 1.21x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 97.9 ms: 1.09x faster                                                 |
| xml_etree_generate   | 54.2 ms                                                | 51.1 ms: 1.06x faster                                                 |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                                 |
| unpickle             | 9.89 us                                                | 9.71 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 71.1 ms: 1.02x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.65 us: 1.01x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| pickle_list          | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| pickle               | 7.35 us                                                | 7.47 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.5 ms: 1.05x slower                                                 |
| python_startup_no_site | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.44 ms: 1.41x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 29.2 ms: 1.27x faster                                                 |
| django_template | 27.3 ms                                                | 21.6 ms: 1.26x faster                                                 |
| genshi_text     | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.59 ms: 1.99x faster                                                 |
| logging_silent          | 119 ns                                                 | 69.3 ns: 1.72x faster                                                 |
| richards                | 51.4 ms                                                | 30.5 ms: 1.68x faster                                                 |
| go                      | 165 ms                                                 | 111 ms: 1.50x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 191 us: 1.49x faster                                                  |
| scimark_lu              | 109 ms                                                 | 74.2 ms: 1.47x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 53.5 ms: 1.46x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 336 ms: 1.46x faster                                                  |
| scimark_sor             | 126 ms                                                 | 87.7 ms: 1.44x faster                                                 |
| raytrace                | 325 ms                                                 | 229 ms: 1.42x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 51.0 ms: 1.42x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.46 ms: 1.42x faster                                                 |
| asyncio_tcp             | 670 ms                                                 | 473 ms: 1.42x faster                                                  |
| nbody                   | 93.3 ms                                                | 66.1 ms: 1.41x faster                                                 |
| mako                    | 10.5 ms                                                | 7.44 ms: 1.41x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 145 us: 1.40x faster                                                  |
| chaos                   | 66.7 ms                                                | 47.8 ms: 1.39x faster                                                 |
| async_tree_none         | 400 ms                                                 | 289 ms: 1.38x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 744 ms: 1.37x faster                                                  |
| pyflate                 | 453 ms                                                 | 331 ms: 1.37x faster                                                  |
| json_dumps              | 8.40 ms                                                | 6.18 ms: 1.36x faster                                                 |
| pycparser               | 916 ms                                                 | 674 ms: 1.36x faster                                                  |
| float                   | 72.4 ms                                                | 53.5 ms: 1.35x faster                                                 |
| tornado_http            | 91.5 ms                                                | 70.0 ms: 1.31x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 26.4 us: 1.30x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.05 ms: 1.30x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.48 ms: 1.29x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.22 ms: 1.29x faster                                                 |
| thrift                  | 580 us                                                 | 453 us: 1.28x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 74.9 ms: 1.28x faster                                                 |
| regex_compile           | 96.4 ms                                                | 75.4 ms: 1.28x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 29.2 ms: 1.27x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 970 ms: 1.27x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 477 ms: 1.27x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.66 us: 1.27x faster                                                 |
| deepcopy                | 281 us                                                 | 222 us: 1.26x faster                                                  |
| django_template         | 27.3 ms                                                | 21.6 ms: 1.26x faster                                                 |
| logging_format          | 4.97 us                                                | 3.95 us: 1.26x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 29.6 ms: 1.25x faster                                                 |
| create_gc_cycles        | 880 us                                                 | 702 us: 1.25x faster                                                  |
| genshi_text             | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                 |
| html5lib                | 44.2 ms                                                | 35.4 ms: 1.25x faster                                                 |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.21 ms: 1.23x faster                                                 |
| fannkuch                | 317 ms                                                 | 258 ms: 1.23x faster                                                  |
| 2to3                    | 201 ms                                                 | 165 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 547 ms: 1.22x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.95 us: 1.22x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 37.0 ms: 1.21x faster                                                 |
| docutils                | 1.78 sec                                               | 1.49 sec: 1.19x faster                                                |
| sqlglot_optimize        | 38.0 ms                                                | 32.1 ms: 1.18x faster                                                 |
| scimark_fft             | 230 ms                                                 | 196 ms: 1.18x faster                                                  |
| generators              | 32.7 ms                                                | 27.9 ms: 1.17x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 63.8 ms: 1.17x faster                                                 |
| mypy2                   | 307 ms                                                 | 262 ms: 1.17x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 472 us: 1.16x faster                                                  |
| sympy_integrate         | 13.3 ms                                                | 11.7 ms: 1.14x faster                                                 |
| unpack_sequence         | 37.4 ns                                                | 32.9 ns: 1.14x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 175 ms: 1.12x faster                                                  |
| coroutines              | 20.2 ms                                                | 18.1 ms: 1.11x faster                                                 |
| sympy_expand            | 275 ms                                                 | 248 ms: 1.11x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.50 sec: 1.11x faster                                                |
| json                    | 3.08 ms                                                | 2.79 ms: 1.11x faster                                                 |
| sympy_str               | 169 ms                                                 | 155 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.17 ms: 1.09x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 97.9 ms: 1.09x faster                                                 |
| regex_v8                | 17.6 ms                                                | 16.2 ms: 1.08x faster                                                 |
| nqueens                 | 68.2 ms                                                | 63.1 ms: 1.08x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.37 us: 1.08x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 72.9 ms: 1.07x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 88.2 ms: 1.06x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 51.1 ms: 1.06x faster                                                 |
| regex_dna               | 162 ms                                                 | 153 ms: 1.05x faster                                                  |
| pathlib                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                                 |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                                 |
| telco                   | 3.63 ms                                                | 3.49 ms: 1.04x faster                                                 |
| unpickle                | 9.89 us                                                | 9.71 us: 1.02x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 71.1 ms: 1.02x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.65 us: 1.01x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| comprehensions          | 17.6 us                                                | 17.7 us: 1.00x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.83 us: 1.01x slower                                                 |
| gc_traversal            | 2.39 ms                                                | 2.43 ms: 1.01x slower                                                 |
| pickle                  | 7.35 us                                                | 7.47 us: 1.02x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.5 ms: 1.05x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.69 ms: 1.10x slower                                                 |
| async_generators        | 234 ms                                                 | 272 ms: 1.16x slower                                                  |
| python_startup_no_site  | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 46.5 ms: 1.17x slower                                                 |
| dask                    | 265 ms                                                 | 325 ms: 1.22x slower                                                  |
| coverage                | 42.0 ms                                                | 59.6 ms: 1.42x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.19x faster                                                          |
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint

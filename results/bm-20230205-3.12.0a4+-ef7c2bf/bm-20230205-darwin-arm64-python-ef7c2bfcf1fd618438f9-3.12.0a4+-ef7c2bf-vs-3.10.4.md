
# Results vs. 3.10.4

- fork: python
- ref: ef7c2bfcf1fd618438f9
- machine: darwin-arm64
- commit hash: ef7c2bf
- commit date: 2023-02-05
- overall geometric mean: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 163 ms: 1.24x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.56 ms: 1.27x faster                                                  |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| html5lib       | 44.2 ms                                                | 34.7 ms: 1.28x faster                                                  |
| tornado_http   | 91.5 ms                                                | 69.3 ms: 1.32x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.0 ms: 1.46x faster                                                  |
| float          | 72.4 ms                                                | 52.0 ms: 1.39x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 72.4 ms: 1.33x faster                                                  |
| regex_v8       | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 191 us: 1.48x faster                                                   |
| json_dumps           | 8.40 ms                                                | 6.11 ms: 1.37x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 156 us: 1.30x faster                                                   |
| xml_etree_process    | 44.8 ms                                                | 34.7 ms: 1.29x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 48.0 ms: 1.13x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 96.4 ms: 1.10x faster                                                  |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 70.1 ms: 1.03x faster                                                  |
| pickle_list          | 2.80 us                                                | 2.74 us: 1.02x faster                                                  |
| unpickle_list        | 2.69 us                                                | 2.66 us: 1.01x faster                                                  |
| pickle_dict          | 17.9 us                                                | 17.9 us: 1.00x slower                                                  |
| pickle               | 7.35 us                                                | 7.46 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.5 ms: 1.05x slower                                                  |
| python_startup_no_site | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.18 ms: 1.46x faster                                                  |
| genshi_xml      | 37.2 ms                                                | 28.3 ms: 1.31x faster                                                  |
| genshi_text     | 18.4 ms                                                | 14.2 ms: 1.29x faster                                                  |
| django_template | 27.3 ms                                                | 21.2 ms: 1.29x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-darwin-arm64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.58 ms: 1.99x faster                                                  |
| logging_silent          | 119 ns                                                 | 65.8 ns: 1.81x faster                                                  |
| richards                | 51.4 ms                                                | 29.8 ms: 1.73x faster                                                  |
| scimark_lu              | 109 ms                                                 | 70.8 ms: 1.54x faster                                                  |
| go                      | 165 ms                                                 | 110 ms: 1.51x faster                                                   |
| async_tree_memoization  | 490 ms                                                 | 327 ms: 1.50x faster                                                   |
| pickle_pure_python      | 283 us                                                 | 191 us: 1.48x faster                                                   |
| scimark_sor             | 126 ms                                                 | 85.5 ms: 1.48x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 53.1 ms: 1.47x faster                                                  |
| raytrace                | 325 ms                                                 | 222 ms: 1.47x faster                                                   |
| hexiom                  | 6.32 ms                                                | 4.32 ms: 1.46x faster                                                  |
| mako                    | 10.5 ms                                                | 7.18 ms: 1.46x faster                                                  |
| chaos                   | 66.7 ms                                                | 45.7 ms: 1.46x faster                                                  |
| asyncio_tcp             | 670 ms                                                 | 459 ms: 1.46x faster                                                   |
| nbody                   | 93.3 ms                                                | 64.0 ms: 1.46x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 49.8 ms: 1.46x faster                                                  |
| async_tree_none         | 400 ms                                                 | 285 ms: 1.41x faster                                                   |
| float                   | 72.4 ms                                                | 52.0 ms: 1.39x faster                                                  |
| pycparser               | 916 ms                                                 | 666 ms: 1.38x faster                                                   |
| json_dumps              | 8.40 ms                                                | 6.11 ms: 1.37x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 743 ms: 1.37x faster                                                   |
| pyflate                 | 453 ms                                                 | 331 ms: 1.37x faster                                                   |
| sqlglot_parse           | 1.37 ms                                                | 1.02 ms: 1.34x faster                                                  |
| regex_compile           | 96.4 ms                                                | 72.4 ms: 1.33x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 25.9 us: 1.33x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.19 ms: 1.32x faster                                                  |
| tornado_http            | 91.5 ms                                                | 69.3 ms: 1.32x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 72.7 ms: 1.32x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 28.3 ms: 1.31x faster                                                  |
| thrift                  | 580 us                                                 | 443 us: 1.31x faster                                                   |
| unpickle_pure_python    | 203 us                                                 | 156 us: 1.30x faster                                                   |
| xml_etree_process       | 44.8 ms                                                | 34.7 ms: 1.29x faster                                                  |
| genshi_text             | 18.4 ms                                                | 14.2 ms: 1.29x faster                                                  |
| django_template         | 27.3 ms                                                | 21.2 ms: 1.29x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 472 ms: 1.28x faster                                                   |
| pprint_pformat          | 1.23 sec                                               | 961 ms: 1.28x faster                                                   |
| deepcopy                | 281 us                                                 | 219 us: 1.28x faster                                                   |
| logging_simple          | 4.63 us                                                | 3.62 us: 1.28x faster                                                  |
| html5lib                | 44.2 ms                                                | 34.7 ms: 1.28x faster                                                  |
| logging_format          | 4.97 us                                                | 3.90 us: 1.27x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.56 ms: 1.27x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 693 us: 1.27x faster                                                   |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.03 ms: 1.26x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.5 ms: 1.26x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.91 us: 1.24x faster                                                  |
| fannkuch                | 317 ms                                                 | 256 ms: 1.24x faster                                                   |
| 2to3                    | 201 ms                                                 | 163 ms: 1.24x faster                                                   |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.80 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 543 ms: 1.23x faster                                                   |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.4 ms: 1.21x faster                                                  |
| scimark_fft             | 230 ms                                                 | 192 ms: 1.20x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.2 ms: 1.19x faster                                                  |
| sqlalchemy_declarative  | 74.9 ms                                                | 63.0 ms: 1.19x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 463 us: 1.18x faster                                                   |
| mypy2                   | 307 ms                                                 | 260 ms: 1.18x faster                                                   |
| comprehensions          | 17.6 us                                                | 15.0 us: 1.17x faster                                                  |
| async_generators        | 234 ms                                                 | 200 ms: 1.17x faster                                                   |
| sympy_str               | 169 ms                                                 | 146 ms: 1.16x faster                                                   |
| sqlglot_normalize       | 196 ms                                                 | 171 ms: 1.14x faster                                                   |
| unpack_sequence         | 37.4 ns                                                | 32.7 ns: 1.14x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 82.0 ms: 1.14x faster                                                  |
| sympy_expand            | 275 ms                                                 | 243 ms: 1.13x faster                                                   |
| xml_etree_generate      | 54.2 ms                                                | 48.0 ms: 1.13x faster                                                  |
| nqueens                 | 68.2 ms                                                | 60.6 ms: 1.12x faster                                                  |
| regex_v8                | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                  |
| json                    | 3.08 ms                                                | 2.78 ms: 1.11x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 96.4 ms: 1.10x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.53 sec: 1.09x faster                                                 |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.08x faster                                                  |
| coroutines              | 20.2 ms                                                | 18.8 ms: 1.07x faster                                                  |
| telco                   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                  |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 70.1 ms: 1.03x faster                                                  |
| pathlib                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 76.2 ms: 1.02x faster                                                  |
| pickle_list             | 2.80 us                                                | 2.74 us: 1.02x faster                                                  |
| unpickle_list           | 2.69 us                                                | 2.66 us: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| pickle_dict             | 17.9 us                                                | 17.9 us: 1.00x slower                                                  |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                                  |
| pickle                  | 7.35 us                                                | 7.46 us: 1.02x slower                                                  |
| generators              | 32.7 ms                                                | 34.4 ms: 1.05x slower                                                  |
| python_startup          | 11.9 ms                                                | 12.5 ms: 1.05x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 45.0 ms: 1.13x slower                                                  |
| python_startup_no_site  | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                  |
| dask                    | 265 ms                                                 | 323 ms: 1.22x slower                                                   |
| coverage                | 42.0 ms                                                | 57.3 ms: 1.36x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint
